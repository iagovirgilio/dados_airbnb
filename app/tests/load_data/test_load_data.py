import pytest
import pandas as pd
from management.commands.load_data import LoadData


def test_run_method(sample_data):
    loader = LoadData(sample_data)

    df_processed = loader.run()

    assert df_processed['name'].iloc[0] == 'Listing1'
    assert df_processed['host_name'].iloc[0] == 'Host1'
    assert df_processed['price'].iloc[0] == 100.0
    assert df_processed['last_review'].iloc[0] == pd.to_datetime('1900-01-01')
    assert df_processed['reviews_per_month'].iloc[0] == 0


def test_run_without_data():
    loader = LoadData()
    with pytest.raises(ValueError):
        loader.run()


def test_load_data_from_csv(test_csv_file):
    loader = LoadData()
    loader.load_data(test_csv_file)

    assert loader.df is not None


def test_load_data_file_not_found():
    loader = LoadData()
    with pytest.raises(FileNotFoundError):
        loader.load_data('arquivo_inexistente.csv')
