import pandas as pd
import logging

class LoadData:
    def __init__(self, data_source=None):
        self.df = None
        if data_source is not None:
            self.load_data(data_source)

    def load_data(self, data_source):
        """Carrega os dados a partir de um arquivo CSV ou de um DataFrame.

        Args:
            data_source: Caminho para o arquivo CSV ou um DataFrame Pandas.
        """
        if isinstance(data_source, pd.DataFrame):
            self.df = data_source
            logging.info("Dados carregados a partir de um DataFrame.")
        elif isinstance(data_source, str):
            try:
                self.df = pd.read_csv(data_source)
                logging.info(f"Dados carregados a partir do arquivo: {data_source}")
            except FileNotFoundError:
                logging.error(f"Arquivo não encontrado: {data_source}")
                raise FileNotFoundError(f"Arquivo não encontrado: {data_source}")
            except pd.errors.ParserError:
                logging.error(f"Erro ao analisar o arquivo: {data_source}")
                raise ValueError(f"Erro ao analisar o arquivo: {data_source}")
        else:
            logging.error("data_source deve ser um caminho de arquivo ou um DataFrame Pandas.")
            raise TypeError("data_source deve ser um caminho de arquivo ou um DataFrame Pandas.")

    def run(self):
        """Executa o processamento dos dados."""
        if self.df is None:
            raise ValueError("Nenhum dado carregado. Use o método load_data() para carregar os dados.")

        self.selecionar_colunas()
        self.tratar_valores_nulos()
        self.remover_caracteres_especiais()
        self.converter_tipos()

        logging.info("Processamento concluído com sucesso.")
        return self.df

    def selecionar_colunas(self):
        """Seleciona e renomeia colunas relevantes."""
        colunas = [
            'id', 'name', 'host_name', 'neighbourhood', 'latitude', 'longitude',
            'room_type', 'price', 'minimum_nights', 'number_of_reviews',
            'last_review', 'reviews_per_month', 'availability_365'
        ]
        self.df = self.df[colunas]
        logging.debug("Colunas selecionadas.")

    def tratar_valores_nulos(self):
        """Trata valores nulos nas colunas especificadas."""
        valores_padrao = {
            'last_review': '1900-01-01',
            'price': 0,
            'reviews_per_month': 0
        }
        for coluna, valor in valores_padrao.items():
            self.df[coluna] = self.df[coluna].fillna(valor)
        logging.debug("Valores nulos tratados.")

    def remover_caracteres_especiais(self):
        """Remove caracteres especiais de colunas de texto."""
        colunas_texto = ['name', 'host_name']
        for coluna in colunas_texto:
           self.df[coluna] = self.df[coluna].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
        logging.debug("Caracteres especiais removidos.")

    def converter_tipos(self):
        """Converte colunas para os tipos apropriados."""
        # Remover símbolos de moeda e converter 'price' para float
        self.df['price'] = self.df['price'].replace({r'\$': '', ',': ''}, regex=True).astype(float)
        # Converter 'last_review' para datetime
        self.df['last_review'] = pd.to_datetime(self.df['last_review'])
        logging.debug("Tipos de dados convertidos.")
