from jugador import Jugador

def test_constructor():
    j = Jugador("Abril",6)
    assert(j.nombre == "Abril")
    assert(j.fichas == 6)

def test_constructor_sin_fichas():
    j = Jugador("Abril")
    assert(j.nombre == "Abril")
    assert(j.fichas == 5)

def test_dar_ficha():
    j = Jugador(10)
    j.darFicha(5)
    assert(j.fichas == 15)

def test_sacarFicha():
    j = Jugador(10)
    j.sacarFicha(5)

def test_tieneFicha():
    j = Jugador(10)
    j.tieneFicha(5)

def test_sinFichas():
    j = Jugador()
    j.sinFichas(0)
    assert(j.fichas == 0)