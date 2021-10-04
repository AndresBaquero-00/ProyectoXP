from project.data import *
from project.calculo import *

data = Data()
calculo = Calculo()

# Prueba que verifica que la data traida mediante petición http
# Sea cargada en el proyecto
def test_request_data() -> None:
    assert data.get_data() != None

