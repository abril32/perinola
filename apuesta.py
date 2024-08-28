class Apuesta:
    def __init__(self):
        self.fichas = 0
    def __repr__(self):
        return f"Apuesta: {self.fichas}"
    def ponerFicha(self):
        self.poner = 1