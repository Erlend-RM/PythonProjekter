from rack import Rack
from node import Node


rack1 = Rack()
node1 = Node(128,2)
node2 = Node(232,2)
node3 = Node(64, 1)

rack1.settInn(node1)
rack1.settInn(node2)
rack1.settInn(node3)

print(rack1.getAntNoder())
print(rack1.antProsRack())
print(rack1.noderMedNokMinne(600))
print(rack1)
