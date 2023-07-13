from node import Node
from rack import Rack
from regneklynge import Regneklynge


def lagNoder(antallNoder, minne, pros):
    for x in range(antallNoder):
        node = Node(minne, pros)
        abel.settInnNode(node)


abel = Regneklynge(12)
noder = lagNoder(650, 64, 1)
noder = lagNoder(16, 1024, 2)


antallPros = abel.antProsessorer()
antallRacks = abel.antRacks()
minne32 = abel.noderMedNokMinne(32)
minne64 = abel.noderMedNokMinne(64)
minne128 = abel.noderMedNokMinne(128)


print(f"Noder med minst 32GB: {minne32}")
print(f"Noder med minst 64GB: {minne64}")
print(f"Noder med minst 128GB: {minne128}")
print(f"Antall prosessorer: {antallPros}")
print(f"Antall rack: {antallRacks}")
