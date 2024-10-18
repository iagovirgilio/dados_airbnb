# Generated by Django 5.1.2 on 2024-10-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0004_fileupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stay',
            name='availability_365',
            field=models.IntegerField(verbose_name='Disponibilidade em 365 dias'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='feels_like',
            field=models.IntegerField(blank=True, null=True, verbose_name='Sensação térmica'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='host_name',
            field=models.CharField(max_length=255, verbose_name='Nome do proprietário'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='humidity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Umidade'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='last_review',
            field=models.DateField(blank=True, null=True, verbose_name='Última avaliação'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='latitude',
            field=models.FloatField(verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='listing_id',
            field=models.IntegerField(verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='longitude',
            field=models.FloatField(verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='minimum_nights',
            field=models.IntegerField(verbose_name='Número mínimo de noites'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='neighbourhood',
            field=models.CharField(max_length=255, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='number_of_reviews',
            field=models.IntegerField(verbose_name='Número de avaliações'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='reviews_per_month',
            field=models.FloatField(blank=True, null=True, verbose_name='Avaliações por mês'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='room_type',
            field=models.CharField(max_length=50, verbose_name='Tipo de quarto'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='temperature',
            field=models.IntegerField(blank=True, null=True, verbose_name='Temperatura ºC'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='weather',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Previsão do tempo'),
        ),
    ]
