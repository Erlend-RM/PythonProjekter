from node import Node
from rack import Rack
from regneklynge import Regneklynge
from datasenter import Datasenter

def hovedprogram():
    datasenter = Datasenter()
    datasenter.lesInnRegneklynge("abel.txt")
    datasenter.lesInnRegneklynge("saga.txt")
    datasenter.skrivUtAlleRegneklynger()

hovedprogram()
