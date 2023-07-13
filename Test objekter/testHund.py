from hund import Hund

def hovedprogram():
    pluto = Hund(5, 15, 10)
    pluto.spring()
    pluto.spis(5)
    print(pluto.vekten())
    pluto.spring()
    pluto.spis(8)
    print(pluto.vekten())
    pluto.spring()
    pluto.spis(8)
    print(pluto.vekten())

hovedprogram()
