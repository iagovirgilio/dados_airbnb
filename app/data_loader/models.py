from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    pass


class Stay(models.Model):
    # Campos dos dados originais
    listing_id = models.IntegerField(verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Nome")
    host_name = models.CharField(max_length=255, verbose_name="Nome do proprietário")
    neighbourhood = models.CharField(max_length=255, verbose_name="Bairro")
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")
    room_type = models.CharField(max_length=50, verbose_name="Tipo de quarto")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    minimum_nights = models.IntegerField(verbose_name="Número mínimo de noites")
    number_of_reviews = models.IntegerField(verbose_name="Número de avaliações")
    last_review = models.DateField(null=True, blank=True, verbose_name="Última avaliação")
    reviews_per_month = models.FloatField(null=True, blank=True, verbose_name="Avaliações por mês")
    availability_365 = models.IntegerField(verbose_name="Disponibilidade em 365 dias")

    # Campo para os dados enriquecidos
    weather = models.CharField(max_length=255, null=True, blank=True, verbose_name="Previsão do tempo")
    feels_like = models.IntegerField(null=True, blank=True, verbose_name="Sensação térmica")
    humidity = models.IntegerField(null=True, blank=True, verbose_name="Umidade")
    temperature = models.IntegerField(null=True, blank=True, verbose_name="Temperatura ºC")

    class Meta:
        verbose_name = "Estadia"
        verbose_name_plural = "Estadias"

    def __str__(self):
        return f'{self.name} by {self.host_name}'


class FileUpload(models.Model):
    FILE_TYPES = (
        ('csv', 'CSV'),
        ('excel', 'Excel'),
    )

    file = models.FileField(upload_to='uploads/', verbose_name="Arquivo")
    uploaded_at = models.DateTimeField(default=timezone.now, verbose_name="Data de envio")
    file_type = models.CharField(max_length=10, choices=FILE_TYPES, default='csv', verbose_name="Tipo de arquivo")

    class Meta:
        verbose_name = "Arquivo"
        verbose_name_plural = "Arquivos"

    def __str__(self):
        return f"{self.file.name} - {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"
