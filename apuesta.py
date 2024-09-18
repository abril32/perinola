class Apuesta:
    def __init__(self):
        self.fichas = 5

    def __repr__(self):
        return f"Apuesta: {self.fichas}"
    
    def ponerFicha(self,cuantas=1):
        self.fichas += cuantas

    def tomarFicha(self,cuantas=1):
        if cuantas > self.fichas:
            raise ValueError("No hay tantas fichas")
        self.fichas -= cuantas
    
    def tomarTodas(self):
        fichasAntes=self.fichas
        self.fichas = 0
        return fichasAntes
    
    def tieneFicha(self, cuantas =1):
        return self.fichas >= cuantas

    def estaVacia(self):
        return self.fichas == 0
