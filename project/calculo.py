class Calculo:
    def sumatoria(self, data: list):
        suma: float = 0
        for d in data:
            suma += float(d)
        
        return suma