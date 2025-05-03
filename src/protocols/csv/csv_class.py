import pandas as pd

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.estado = None
        self.df_filtrado = None

    def load_csv(self):
        self.df = pd.read_csv(self.file_path)
    
    def filter_by(self, collumn: str, attribute: str):
        self.df_filtrado = self.df[self.df[collumn] == attribute]
        return self.df_filtrado
    
    def sub_filter(self, collumn: str, attribute: str):
        return self.df_filtrado[self.df_filtrado[collumn] == attribute]

    def recursive_filter(self, columns: list, attributes: list):
        if len(columns) != len(attributes):
            raise ValueError("Length collumns and attributes not equal")
        
        if len(columns) == 0:
            return self.df
        
        initial_collumn = columns[0]
        initial_attribute = attributes[0]

        df_recursive = self.df[self.df[initial_collumn] == initial_attribute]

        print(len(columns))
        
        if len(columns) == 1:
            return df_recursive
        else:
            return self.recursive_filter(columns[1:], attributes[1:])