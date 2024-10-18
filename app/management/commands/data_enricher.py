import os
import sys
# Configurar o caminho do projeto
sys.path.append('/usr/src/app')
# Definir a variável de ambiente para as configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airbnb_project.settings')
# Inicializar o Django
import django
django.setup()

import asyncio
import aiohttp
import pandas as pd
import logging
from load_data import LoadData
from data_server import DataSaver  # Certifique-se de que o caminho está correto


class DataEnricher:
    def __init__(self, df):
        self.df = df

    async def fetch_weather(self, session, lat, lon):
        """Faz uma chamada assíncrona à API do OpenWeatherMap para obter dados meteorológicos."""
        api_key = os.environ.get("OPEN_WEATHER_KEY")
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=pt_br'

        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    # Extrair campos específicos
                    weather_info = {
                        'temperature': data.get('main', {}).get('temp'),
                        'feels_like': data.get('main', {}).get('feels_like'),
                        'humidity': data.get('main', {}).get('humidity'),
                        'weather': data.get('weather', [{}])[0].get('description')
                    }
                    return weather_info
                else:
                    logging.error(f'Erro na API: {response.status} ao obter dados para lat={lat}, lon={lon}')
                    return None
        except Exception as e:
            logging.error(f'Exceção ao obter dados meteorológicos: {e}')
            return None

    async def fetch_weather_with_semaphore(self, session, lat, lon, semaphore):
        async with semaphore:
            try:
                return await self.fetch_weather(session, lat, lon)
            except Exception as e:
                logging.error(f"Erro ao obter dados meteorológicos para lat={lat}, lon={lon}: {e}")
                return {key: None for key in ['temperature', 'feels_like', 'humidity', 'weather']}

    async def enrich_data_async(self):
        listings = self.df.to_dict('records')

        semaphore = asyncio.Semaphore(1)  # Limitar a 50 chamadas simultâneas
        async with aiohttp.ClientSession() as session:
            tasks = []
            for listing in listings:
                lat = listing['latitude']
                lon = listing['longitude']
                task = self.fetch_weather_with_semaphore(session, lat, lon, semaphore)
                tasks.append(task)
            weather_data_list = await asyncio.gather(*tasks)

        # Substituir None por dicionários com valores None
        default_weather_keys = ['temperature', 'feels_like', 'humidity', 'weather']
        weather_data_list = [
            data if data is not None else {key: None for key in default_weather_keys}
            for data in weather_data_list
        ]

        # Adicionar os dados meteorológicos ao DataFrame
        weather_df = pd.DataFrame(weather_data_list)
        self.df = pd.concat([self.df.reset_index(drop=True), weather_df.reset_index(drop=True)], axis=1)
        logging.info("Dados enriquecidos com sucesso.")

    def enrich_data(self):
        asyncio.run(self.enrich_data_async())


if __name__ == '__main__':
    # Carregar os dados
    dados = LoadData('management/commands/listings.csv')
    dados_t = dados.run()

    # Enriquecer os dados
    enricher = DataEnricher(dados_t)
    enricher.enrich_data()

    print("=" * 100)
    print(enricher.df)
    print("=" * 100)

    # Salvar os dados no banco de dados
    saver = DataSaver(enricher.df)
    saver.save_to_database()

    print("-" * 100)
    print(enricher.df.head())  # Exibir as primeiras linhas do DataFrame enriquecido
    print("-" * 100)
