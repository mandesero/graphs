from pygmlparser.Parser import Parser

PATH = '/home/mandesero/Desktop/Graph/AttMpls.gml'

parser = Parser()
parser.loadGML(path=PATH)
parser.parse()

from numpy.random import random, randint

with open('nodes.csv', 'w', encoding='utf-8') as file:
    # file.write(":ID,label,country,longitude,internal,latitude,type,:LABEL\n")
    s = "CREATE "
    for node in parser.graph.graphNodes.values():
        # file.write(f'{node.id},"{node.label}","{node.Country}",{node.Longitude},{node.Internal},{node.Latitude},"{node.type}",Node\n')
        s += f'(node_{node.id} :Node {{ id:{node.id}, label:"{node.label}", country:"{node.Country}", longitude:{node.Longitude}, internal:{node.Internal}, latitude:{node.Latitude}, type:"{node.type}"}}),\n'
    for edge in parser.graph.graphEdges:
        i, j, k = randint(5,50), random(), random()
        s += f'(node_{edge.source})-[:{edge.LinkLabel.split()[0]} {{ cost:{i}, reliability:{j}, jitter:{k / 10} }}]->(node_{edge.target}),\n'
        s += f'(node_{edge.source})<-[:{edge.LinkLabel.split()[0]} {{ cost:{i}, reliability:{j}, jitter:{k / 10} }}]-(node_{edge.target}),\n'
    file.write(s[:-2])





# with open('edges.csv', 'w', encoding='utf-8') as file:
#     file.write(":START_ID,:END_ID,:TYPE\n")
#     for edge in parser.graph.graphEdges:
#
#         file.write(f'{edge.source},{edge.target},"{edge.LinkLabel}",Edge\n')
# for edge in parser.graph.graphEdges:
#     s += f'(node_{edge.source})-[:{edge.LinkLabel}]->(node_{edge.target}),\n'