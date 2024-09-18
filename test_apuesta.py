from apuesta import Apuesta

def test_ponerFicha():
    a = Apuesta()
    a.ponerFicha(3)
    assert (a.fichas == 8)

def test_tomarFicha():
    a = Apuesta()
    a.tomarFicha(1)
    assert (a.fichas == 4)

def test_tomarTodas():
    a = Apuesta()
    a.tomarTodas()
    assert(a.fichas == 0)
    assert(a.fichasAntes == 5)

def test_tieneFicha():
    a = Apuesta()
    a.tieneFicha
    assert (a.fichas)

def test_estaVacia():
    a = Apuesta()
    a.estaVacia()
    assert (a.fichas == 0)
