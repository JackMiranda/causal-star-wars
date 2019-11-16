from networkx import DiGraph
import networkx.algorithms.dag as algs

def DAG_check(dag, f, *args):
    f(*args)
    if not algs.is_directed_acyclic_graph(dag):
        raise Exception(F'Call to {f} violates the acyclic condition')

add_node = lambda node, dag: DAG_check(dag, dag.add_node, node)
add_edge = lambda l, r, dag: DAG_check(dag, dag.add_edge, l, r)

D = DiGraph()
add_edge('Luke has the Force', 'Luke is a skilled pilot', D)
add_edge('Luke has the Force', 'Luke lands the shot', D)
add_edge('Luke is a skilled pilot', 'Luke lands the shot', D)

        
print(D.nodes)
print([n for n in D.successors('Luke has the Force')])
