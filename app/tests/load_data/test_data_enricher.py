import pytest
import pandas as pd
from unittest.mock import patch, AsyncMock, MagicMock
from management.commands.data_enricher import DataEnricher


def test_enrich_data(sample_data):
    # Configuração
    enricher = DataEnricher(sample_data)

    # Mock da chamada à API
    weather_mock = {
        'temperature': 27.52,
        'feels_like': 30.56,
        'humidity': 77,
        'weather': 'nuvens dispersas'
    }

    async def mock_fetch_weather(self, session, lat, lon):
        return weather_mock

    with patch.object(DataEnricher, 'fetch_weather', new=mock_fetch_weather):
        # Ação
        enricher.enrich_data()

    # Verificação
    df_enriched = enricher.df
    assert 'temperature' in df_enriched.columns
    assert 'feels_like' in df_enriched.columns
    assert 'humidity' in df_enriched.columns
    assert 'weather' in df_enriched.columns
    assert df_enriched['temperature'].iloc[0] == 27.52
    assert df_enriched['weather'].iloc[0] == 'nuvens dispersas'


def test_enrich_data_api_error(sample_data):
    # Configuração
    enricher = DataEnricher(sample_data)
    
    # Mock da chamada à API que retorna None (simulando um erro)
    async def mock_fetch_weather(self, session, lat, lon):
        return None  # Simula falha na API

    with patch.object(DataEnricher, 'fetch_weather', new=mock_fetch_weather):
        # Ação
        enricher.enrich_data()
    
    # Verificação
    df_enriched = enricher.df
    assert 'temperature' in df_enriched.columns
    assert df_enriched['temperature'].isnull().all()


def test_enrich_data_exception(sample_data):
    # Configuração
    enricher = DataEnricher(sample_data)
    
    # Mock da chamada à API que levanta uma exceção
    async def mock_fetch_weather(self, session, lat, lon):
        raise Exception("Erro de rede")

    with patch.object(DataEnricher, 'fetch_weather', new=mock_fetch_weather):
        # Ação
        enricher.enrich_data()
    
    # Verificação
    df_enriched = enricher.df
    assert 'temperature' in df_enriched.columns
    assert df_enriched['temperature'].isnull().all()


# @pytest.mark.asyncio
# async def test_fetch_weather():
#     # Configuração
#     enricher = DataEnricher(pd.DataFrame())
#     lat, lon = 0, 0

#     # Dados simulados da resposta da API
#     mock_response_data = {
#         'main': {
#             'temp': 27.52,
#             'feels_like': 30.56,
#             'humidity': 77
#         },
#         'weather': [
#             {
#                 'description': 'nuvens dispersas'
#             }
#         ]
#     }

#     # Mock do objeto de resposta
#     mock_response = AsyncMock()
#     mock_response.status = 200
#     mock_response.json.return_value = mock_response_data

#     # Configurar o mock para session.get
#     mock_session = AsyncMock()
#     mock_session.get.return_value.__aenter__.return_value = mock_response

#     # Usar o mock_session no teste
#     weather_data = await enricher.fetch_weather(mock_session, lat, lon)

#     # Verificação
#     assert weather_data['temperature'] == 27.52
#     assert weather_data['feels_like'] == 30.56
#     assert weather_data['humidity'] == 77
#     assert weather_data['weather'] == 'nuvens dispersas'
