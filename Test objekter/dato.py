class Dato:

    def __init__(self, nyDag, nyMaaned, nyttAar):
        self._nyDag = int(nyDag)
        self._nyMaaned = int(nyMaaned)
        self._nyttAar = int(nyttAar)

    def dag(self):
        return self._nyDag

    def lesAar(self):
        return self._nyttAar

    def strengDato(self):
        return f"{self._nyDag}.{self._nyMaaned}.{self._nyttAar}"

    def mai17(self):
        if self._nyDag == 17:
            if self._nyMaaned == 5:
                return True
            else:
                return False
        else:
            return False
