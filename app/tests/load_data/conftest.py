import os
import pytest
import pandas as pd


@pytest.fixture
def test_csv_file():
    data_source = 'tests/load_data/test_data.csv'
    # Criar o arquivo CSV de teste
    df_sample = pd.DataFrame({
        'id': [1, 2],
        'name': ['Listing@1', 'Listing*2'],
        'host_name': ['Host#1', 'Host&2'],
        'neighbourhood': ['Neighbourhood 1', 'Neighbourhood 2'],
        'latitude': [40.0, 41.0],
        'longitude': [-70.0, -71.0],
        'room_type': ['Private room', 'Entire home/apt'],
        'price': ['$100', '$150'],
        'minimum_nights': [2, 3],
        'number_of_reviews': [10, 20],
        'last_review': [None, '2021-02-01'],
        'reviews_per_month': [None, 0.4],
        'availability_365': [200, 150]
    })
    df_sample.to_csv(data_source, index=False)
    yield data_source
    # Remover o arquivo após o teste
    os.remove(data_source)


@pytest.fixture
def sample_data():
    data = {
        'id': [1, 2],
        'name': ['Listing@1', 'Listing*2'],
        'host_name': ['Host#1', 'Host&2'],
        'neighbourhood': ['Neighbourhood 1', 'Neighbourhood 2'],
        'latitude': [40.0, 41.0],
        'longitude': [-70.0, -71.0],
        'room_type': ['Private room', 'Entire home/apt'],
        'price': ['$100', '$150'],
        'minimum_nights': [2, 3],
        'number_of_reviews': [10, 20],
        'last_review': [None, '2021-02-01'],
        'reviews_per_month': [None, 0.4],
        'availability_365': [200, 150]
    }
    return pd.DataFrame(data)
