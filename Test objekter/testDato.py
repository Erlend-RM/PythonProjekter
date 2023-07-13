from dato import Dato

def hovedprogram():
    dato = Dato(15, 10, 2021)
    print(dato.lesAar())
    if dato.dag() == 15:
        print("Løningspils!")
    elif dato.dag() == 1:
        print("Ny måned, nye mulighet!")
    dagensDato = dato.strengDato()
    print(dagensDato)

hovedprogram()
