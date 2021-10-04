from project.data import *
import pandas

class Filter:
    data: list = None
    def __init__(self) -> None:
        self.data: pandas.DataFrame = Data().get_data()
    
    def get_unique(self, label: str) -> pandas.Series:
        return self.data[label].unique()

    def get_grouped_area_sembrada(self, label: str):
        return self.data.groupby(label)['Area Sembrada (ha)']

    def get_grouped_area_cosechada(self, label: str):
        return self.data.groupby(label)['Area Cosechada (ha)']

    def get_grouped_produccion(self, label: str):
        return self.data.groupby(label)['Producción (t)']

    def get_field(self, label: str) -> pandas.Series:
        return self.data[label]

    def get_row(self, object, index) -> pandas.Series:
        return object.iloc[index]
    
