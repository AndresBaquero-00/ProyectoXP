from project.charts import *
from project.data import *
from project.filters import *
from project.analysis import *

data = Data()
datos = data.get_data()

filters = Filter(datos)
departments = filters.get_departments()

anaylsis = Anaylsis()
charts = Charts()

asbd: list = []
for i in departments:
    conjunto: dict = dict(department = i, area_sembrada = filters.get_area_sembrada_by_department(i))
    asbd.append(conjunto)

asbd_a = anaylsis.sort_by_area_sembrada(asbd)

charts.horizontal_bar(asbd_a[0], asbd_a[1], 'Area Sembrada')





