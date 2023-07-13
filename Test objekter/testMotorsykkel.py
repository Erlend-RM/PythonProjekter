from motorsykkel import Motorsykkel

def hovedprogram():
    mc1 = Motorsykkel("Honda", "AB12345", 250)
    mc2 = Motorsykkel("BMW", "TC69699", 125)
    mc3 = Motorsykkel("Harley-Davidson", "MC42069", 590)
    mc1.skrivUt()
    mc2.skrivUt()
    mc3.skrivUt()
    mc3.kjor(10)
    print(mc3.hentKilometerstand())

hovedprogram()
