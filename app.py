from flask import Flask, render_template
from project.analysis import Analysis
from project.charts import *

app = Flask(__name__)

analysis = Analysis()
chart = Charts()

@app.route('/home')
def home():
    area_sembrada = analysis.area_sembrada_por_departamento()
    produccion = analysis.produccion_por_departamento()
    chart_area_sembrada_bar = chart.horizontal_bar(area_sembrada.index, area_sembrada, 'Área Sembrada (Hectáreas)')
    chart_produccion_bar = chart.horizontal_bar(produccion.index, produccion, 'Producción (Toneladas)')
    area_cultivada_total = f'{analysis.area_cultivada():.0f} ha'
    produccion_total = f'{analysis.produccion_total():.0f} t'
    cosechada_promedio = f'{analysis.area_cosechada_promedio():.0f} ha'

    return render_template(
        'home.html',
        cultivada_total = area_cultivada_total,
        produccion_total = produccion_total,
        cosechada_promedio = cosechada_promedio,
        chart_area_sembrada_bar = chart_area_sembrada_bar,
        chart_produccion_bar = chart_produccion_bar
    )

if __name__ == '__main__':
    app.run(debug = True)
