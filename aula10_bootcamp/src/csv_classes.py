import pandas as pd 


class CsvProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_csv(self):
        self.df = pd.read_csv(self.file_path)

    def filter_by_estado(self, coluna, atributo):
        return self.df[self.df[coluna] == atributo]

