# Generated by Django 5.1.2 on 2024-10-17 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='stay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('host_name', models.CharField(max_length=255)),
                ('neighbourhood', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('room_type', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('minimum_nights', models.IntegerField()),
                ('number_of_reviews', models.IntegerField()),
                ('last_review', models.DateField(blank=True, null=True)),
                ('reviews_per_month', models.FloatField(blank=True, null=True)),
                ('availability_365', models.IntegerField()),
                ('weather_main', models.CharField(blank=True, max_length=255, null=True)),
                ('weather_description', models.CharField(blank=True, max_length=255, null=True)),
                ('weather_icon', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
