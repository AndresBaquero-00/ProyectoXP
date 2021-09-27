from project.calculo import *

class Anaylsis:
    calculo: Calculo

    def __init__(self) -> None:
        self.calculo = Calculo()
    
    def sort_by_area_sembrada(self, data: list) -> tuple:
        departments: list = []
        area_s: list = []

        for i in data:
            departments.append(i['department'])
            area_s.append(self.calculo.sumatoria(i['area_sembrada']))

        area_s, departments = self.sort(area_s, departments)

        return departments, area_s

    def sort(self, a: list, b: list) -> tuple:
        for i in range(len(a)):
            for j in range(i, len(a)):
                if a[i] > a[j]:
                    temp = a[i]
                    tempo = b[i]

                    a[i] = a[j]
                    b[i] = b[j]

                    a[j] = temp
                    b[j] = tempo

        return a, b
