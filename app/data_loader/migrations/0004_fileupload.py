# Generated by Django 5.1.2 on 2024-10-18 02:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0003_alter_stay_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('file_type', models.CharField(choices=[('csv', 'CSV'), ('excel', 'Excel')], max_length=10)),
            ],
        ),
    ]
