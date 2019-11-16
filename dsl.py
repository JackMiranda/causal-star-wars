from itertools import combinations
import pickle
import sys

import networkx.algorithms as algs
from networkx import DiGraph


def check_line(line):
    if len(line) != 2:
        raise Exception(f'invalid format: {" ".join(line)}')
    return True


def parse(filename):
    d = DiGraph()
    with open(filename) as file:
        d.add_edges_from(map(lambda l: (l[0].strip(), l[1].strip()), filter(check_line, [l.split('->') for l in file])))
        if not algs.is_directed_acyclic_graph(d):
            raise Exception('Parsed graph violates the acyclic condition')
        # Add empty probability tables
        for n in d.nodes:
            d.add_node(n, prob=[])
        return d


def prompt_probabilities(dag):
    for n in dag.nodes:
        pred = list(DiGraph.predecessors(dag, n))
        for i in range(1, len(pred)):
            for c in combinations(pred, i):
                prob = float(input(f'What is the probability that {n}, if {", and ".join(c)}? '))
                dag.nodes[n]['prob'].append((set(c), prob))

        # Special cases are a code smell
        if not len(pred) == 0:
            dag.nodes[n]['prob'].append((set(pred), 1))
            prob = float(input(f'What is the probability that {n} if none of these is true: {", and ".join(pred)}? '))
            dag.nodes[n]['prob'].append((set([]), prob))
    return dag


def lookup_prob(dag, n, S):
    return next(p for (s, p) in dag.nodes[n]['prob'] if S == s)


def print_probabilities(dag):
    for n in dag.nodes:
        pred = list(DiGraph.predecessors(dag, n))
        for i in range(len(pred)):
            for c in combinations(pred, i):
                msg = ", and ".join(c) if len(c) > 0 else "no causes are true"
                false = set(pred) - set(c)
                print(
                    f'The probability that {n} when {msg}, but NOT {", and ".join(false)} is: {lookup_prob(dag, n, set(c))}')


dag = parse('graph')
if not len(sys.argv) > 1:
    dag = prompt_probabilities(dag)
with open('graph.pickle','wb') as f:
    pickle.dump(dag, f)
    print('Written to graph.pickle')
