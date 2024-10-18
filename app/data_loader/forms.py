from django import forms
from .models import FileUpload

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file', 'file_type']

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        if file:
            if file.size > 10 * 1024 * 1024:
                raise forms.ValidationError("O arquivo é muito grande ( >10MB ).")
            if not file.name.endswith(('.csv', '.xlsx', '.xls')):
                raise forms.ValidationError("Formato de arquivo inválido. Apenas CSV e Excel são permitidos.")
            return file
        else:
            raise forms.ValidationError("Nenhum arquivo foi enviado.")
