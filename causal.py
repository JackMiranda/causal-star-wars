from networkx import DiGraph
import networkx.algorithms.dag as algs

def DAG_check(dag, f, *args):
    f(*args)
    if not algs.is_directed_acyclic_graph(dag):
        raise Exception(F'Call to {f} violates the acyclic condition')

DAG_add_node = lambda node, dag: DAG_check(dag, dag.add_node, node)
DAG_add_edge = lambda l, r, dag: DAG_check(dag, dag.add_edge, l, r)

D = DiGraph()
DAG_add_node('Luke has the Force', D)
DAG_add_node('Luke is a skilled pilot', D)
DAG_add_edge('Luke has the Force', 'Luke is a skilled pilot', D)
DAG_add_edge('Luke is a skilled pilot', 'Luke has the Force', D)

print(D.edges)
