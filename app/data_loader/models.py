from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    pass


class Stay(models.Model):
    # Campos dos dados originais
    listing_id = models.IntegerField()
    name = models.CharField(max_length=255)
    host_name = models.CharField(max_length=255)
    neighbourhood = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    room_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    minimum_nights = models.IntegerField()
    number_of_reviews = models.IntegerField()
    last_review = models.DateField(null=True, blank=True)
    reviews_per_month = models.FloatField(null=True, blank=True)
    availability_365 = models.IntegerField()

    # Campo para os dados enriquecidos
    weather = models.CharField(max_length=255, null=True, blank=True)
    feels_like = models.IntegerField(null=True, blank=True)
    humidity = models.IntegerField(null=True, blank=True)
    temperature = models.IntegerField(null=True, blank=True)

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

    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(default=timezone.now)
    file_type = models.CharField(max_length=10, choices=FILE_TYPES)

    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.file.name} - {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"
