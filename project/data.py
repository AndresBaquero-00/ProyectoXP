import requests

class Data:
    url = 'https://www.datos.gov.co/resource/p5fp-pay3.json'
    def get_data(self) -> list:
        return requests.get(self.url).json()
