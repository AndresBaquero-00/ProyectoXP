from pandas.core.frame import DataFrame
import requests
import pandas

class Data:
    #url = 'https://www.datos.gov.co/resource/p5fp-pay3.json'
    def get_data(self) -> pandas.DataFrame:
        return pandas.read_csv('https://www.datos.gov.co/api/views/p5fp-pay3/rows.csv?accessType=DOWNLOAD')
