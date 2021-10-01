from flask import Flask, render_template
from project.analysis import Anaylsis

app = Flask(__name__)

analysis = Anaylsis()

@app.route('/home')
def home():
    chart_area_sembrada_bar = analysis.sort_by_area_sembrada('bar')
    chart_area_sembrada_pie = analysis.sort_by_area_sembrada('pie', 8)
    return render_template(
        'home.html',
        cultivada_promedio = '5000 ha',
        produccion_total = '10000 t',
        cosechada_promedio = '8500 ha',
        chart_area_sembrada_bar = chart_area_sembrada_bar,
        chart_area_sembrada_pie = chart_area_sembrada_pie
    )

if __name__ == '__main__':
    app.run(debug = True)
