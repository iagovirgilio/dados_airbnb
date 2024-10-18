import pandas as pd
from django.db import transaction

from data_loader.models import Stay


class DataSaver:
    def __init__(self, df):
        self.df = df

    def save_to_database(self):
        """Salva os dados do DataFrame no banco de dados."""
        # Converter 'last_review' para datetime, se ainda não foi feito
        self.df['last_review'] = pd.to_datetime(self.df['last_review'], errors='coerce')

        # Obter os listing_ids existentes
        existing_listing_ids = set(Stay.objects.values_list('listing_id', flat=True))
    
        new_stays = []
        updated_stays = []

        for index, row in self.df.iterrows():
            stay_data = {
                'listing_id': row['id'],
                'name': row['name'],
                'host_name': row['host_name'],
                'neighbourhood': row['neighbourhood'],
                'latitude': row['latitude'],
                'longitude': row['longitude'],
                'room_type': row['room_type'],
                'price': row['price'],
                'minimum_nights': row['minimum_nights'],
                'number_of_reviews': row['number_of_reviews'],
                'last_review': row['last_review'],
                'reviews_per_month': row['reviews_per_month'],
                'availability_365': row['availability_365'],
                'weather': row['weather'],
                'feels_like': row['feels_like'],
                'humidity': row['humidity'],
                'temperature': row['temperature'],
            }

            if row['id'] in existing_listing_ids:
                # Atualizar registro existente
                stay = Stay.objects.get(listing_id=row['id'])
                for field, value in stay_data.items():
                    setattr(stay, field, value)
                updated_stays.append(stay)
            else:
                # Criar novo registro
                stay = Stay(**stay_data)
                new_stays.append(stay)

        batch_size = 1000

        # Salvar novos registros
        if new_stays:
            with transaction.atomic():
                for i in range(0, len(new_stays), batch_size):
                    Stay.objects.bulk_create(new_stays[i:i+batch_size], batch_size=batch_size)

        # Atualizar registros existentes
        if updated_stays:
            with transaction.atomic():
                for i in range(0, len(updated_stays), batch_size):
                    Stay.objects.bulk_update(
                        updated_stays[i:i+batch_size],
                        fields=[
                            'name', 'host_name', 'neighbourhood', 'latitude', 'longitude',
                            'room_type', 'price', 'minimum_nights', 'number_of_reviews',
                            'last_review', 'reviews_per_month', 'availability_365',
                            'weather', 'feels_like', 'humidity', 'temperature'
                        ],
                        batch_size=batch_size
                    )
        print("Dados salvos no banco de dados com sucesso.")
