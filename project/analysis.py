from project.calculo import *
from project.charts import *
from project.filters import *

class Anaylsis:
    calculo: Calculo
    filters: Filter
    charts: Charts

    def __init__(self) -> None:
        self.calculo = Calculo()
        self.filters = Filter()
        self.charts = Charts()
    
    def sort_by_area_sembrada(self, chart_type: str, n: int = 0) -> str:
        departments: list = self.filters.get_departments()
        area_s: list = [ self.calculo.sumatoria(self.filters.get_area_sembrada_by_department(i)) for i in departments ]

        departments, area_s = self.sort(area_s, departments)

        if n > 0:
            res: list = area_s[n:]
            departments = departments[0:n]
            area_s = area_s[0:n]

            departments.append('Otros')
            area_s.append(self.calculo.sumatoria(res))

        if chart_type == 'bar':
            return self.charts.horizontal_bar(departments, area_s,'Area Sembrada (Hectareas)')
        elif chart_type == 'pie':
            return self.charts.pie_chart(departments, area_s,'Area Sembrada por cada Departamento')
        else:
            return 'none'

    def sort(self, a: list, b: list) -> tuple:
        for i in range(len(a)):
            for j in range(i, len(a)):
                if a[i] < a[j]:
                    temp = a[i]
                    tempo = b[i]

                    a[i] = a[j]
                    b[i] = b[j]

                    a[j] = temp
                    b[j] = tempo

        return b, a
