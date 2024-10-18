import pandas as pd

from django.contrib import messages
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.shortcuts import get_object_or_404, redirect
from django.urls import path, reverse
from django.utils.html import format_html

from data_loader.forms import FileUploadForm
from .models import FileUpload
from .models import CustomUser, Stay

from management.commands.data_enricher import DataEnricher
from management.commands.data_server import DataSaver
from management.commands.load_data import LoadData


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Stay)
class StayAdmin(admin.ModelAdmin):
    list_display = ('listing_id', 'name', 'host_name', 'neighbourhood', 'price', 'price_category', 'availability_365', 'monthly_occupancy', 'temperature')
    list_filter = ('neighbourhood', 'room_type', 'availability_365')
    search_fields = ('name', 'host_name', 'neighbourhood')
    ordering = ('-price',)

    @admin.display(description='Ocupação Mensal')
    def monthly_occupancy(self, obj):
        occupied_days = 365 - obj.availability_365
        occupancy_rate = (occupied_days / 365) * 100
        return f"{occupancy_rate:.1f}%"

    def price_category(self, obj):
        if obj.price < 100:
            return 'Barato'
        elif obj.price < 300:
            return 'Moderado'
        else:
            return 'Caro'
    price_category.short_description = 'Categoria de Preço'


@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    form = FileUploadForm
    list_display = ('file', 'uploaded_at', 'file_type', 'process_button')
    list_filter = ('file_type', 'uploaded_at')
    search_fields = ('file__icontains',)

    # Definindo URLs personalizadas dentro do admin
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:fileupload_id>/process/',
                self.admin_site.admin_view(self.process_file),
                name='data_loader_fileupload_process',
            ),
        ]
        return custom_urls + urls

    # Método para gerar o botão "Processar"
    def process_button(self, obj):
        return format_html(
            '<a class="button btn btn-sm btn-primary" href="{}" onclick="return confirm(\'Tem certeza de que deseja processar este arquivo?\');">Processar</a>',
            reverse('admin:data_loader_fileupload_process', args=[obj.id])
        )
    process_button.short_description = 'Ações'
    process_button.allow_tags = True

    # View personalizada para processar o arquivo
    def process_file(self, request, fileupload_id, *args, **kwargs):
        file_upload = get_object_or_404(FileUpload, id=fileupload_id)

        try:
            # Ler o arquivo no DataFrame
            if file_upload.file_type == 'csv':
                df = pd.read_csv(file_upload.file.path)
            elif file_upload.file_type == 'excel':
                df = pd.read_excel(file_upload.file.path)
            else:
                self.message_user(request, "Tipo de arquivo inválido.", level=messages.ERROR)
                return redirect(reverse('admin:data_loader_fileupload_changelist'))

            # Processar os dados usando suas classes
            load_data = LoadData(df)
            dados_t = load_data.run()

            enricher = DataEnricher(dados_t)
            enricher.enrich_data()

            saver = DataSaver(enricher.df)
            saver.save_to_database()

            self.message_user(request, f"Arquivo '{file_upload.file.name}' processado com sucesso.", level=messages.SUCCESS)
        except Exception as e:
            self.message_user(request, f"Erro ao processar o arquivo '{file_upload.file.name}': {str(e)}", level=messages.ERROR)

        # Redirecionar para a listagem de arquivos
        return redirect(reverse('admin:data_loader_stay_changelist'))
