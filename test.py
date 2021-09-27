from project.data import *
from project.calculo import *

data = Data()
calculo = Calculo()

# Prueba que verifica que la data traida mediante petición http
# Sea cargada en el proyecto
def test_request_data() -> None:
    assert data.get_data() != None

# Prueba que verifica que la suma de unos datos genéricos
# Sea correcta
def test_sumatoria() -> None:
    assert calculo.sumatoria(['1', '1.5', '4.5']) == 7