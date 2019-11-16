import json

from networkx.readwrite import json_graph
import pickle
from networkx import DiGraph

with open('graph.pickle','rb') as f:
    dag = pickle.load(f)

for n in dag.nodes:
    dag.nodes[n]['prob'] = []

with open('graph.json','w') as f:
    f.write(json.dumps(json_graph.node_link_data(dag)))
    print('Written to graph.json')
