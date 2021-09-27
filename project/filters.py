class Filter:
    data: list = None
    def __init__(self, data: list) -> None:
        self.data = data
    
    def get_departments(self) -> list:
        rows: list = []
        for dato in self.data:
            if rows.count(dato['departamento']) == 0:
                rows.append(dato['departamento'])
        return rows

    def get_cultivos(self) -> list:
        rows: list = []
        for dato in self.data:
            if rows.count(dato['cultivo']) == 0:
                rows.append(dato['cultivo'])
        return rows

    def get_area_sembrada_by_department(self, department: str) -> list:
        rows: list = []
        for dato in self.data:
            if dato['departamento'] == department:
                rows.append(dato['area_sembrada_ha'])

        return rows
    
