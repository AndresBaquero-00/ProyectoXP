from project.util import *
from project.filters import *

class Analysis:

    def __init__(self) -> None:
        self.util = Util()
        self.filters = Filter()

    def departamentos(self) -> list:
        return list(self.filters.get_unique('Departamento'))
    
    def area_sembrada_por_departamento(self) -> pandas.Series:
        fdata = self.filters.get_grouped_area_sembrada('Departamento')
        fdata = self.util.sum(fdata)
        fdata = self.util.sort(fdata)
        return fdata

    def produccion_por_departamento(self) -> pandas.Series:
        fdata = self.filters.get_grouped_produccion('Departamento')
        fdata = self.util.sum(fdata)
        fdata = self.util.sort(fdata)
        return fdata
    
    def area_cultivada(self) -> float:
        fdata = self.filters.get_field('Area Sembrada (ha)')
        return self.util.sum(fdata)

    def area_cosechada_promedio(self) -> float:
        fdata = self.filters.get_grouped_area_cosechada('Departamento')
        fdata = self.util.sum(fdata)
        return self.util.mean(fdata)

    def produccion_total(self) -> float:
        fdata = self.filters.get_grouped_produccion('Año')
        fdata = self.util.sum(fdata)
        return self.filters.get_row(fdata, 0)



