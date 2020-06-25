import operator

import GraphTools

g = GraphTools.load_graph_from_txt("Slashdot0902.txt")
print('Graph Nodes: %d, Edges: %d' % (g.GetNodes(), g.GetEdges()))

g = GraphTools.deferred_decisions_with_uniform_probability(g)

g = GraphTools.constant_threshold_assignment(g, 2)

print('After Deferred decision Nodes: %d, Edges: %d' % (g.GetNodes(), g.GetEdges()))

seed_set = []

threshold_table = {}
degree_table = {}


def calculate_tables():

    for node in g.Nodes():
        n_id = node.GetId()
        n_threshold = g.GetIntAttrDatN(n_id, "threshold")
        n_out_degree = node.GetOutDeg()
        threshold_table[n_id] = n_threshold
        degree_table[n_id] = n_out_degree


def get_maximum_degree_node_id():
    return max(degree_table.items(), key=operator.itemgetter(1))[0]


def get_maximum_threshold_node_id():
    return max(threshold_table.items(), key=operator.itemgetter(1))[0]


calculate_tables()


def update_nodes(x):
    i = 0

    for out_node in g.GetNI(x).GetOutEdges():

        out_threshold = g.GetIntAttrDatN(out_node, "threshold")
        if out_threshold > 0:
            i = i + 1
        if degree_table[out_node] > 0:
            degree_table[out_node] = degree_table[out_node] - 1
        threshold_table[out_node] = threshold_table[out_node] - 1

    degree_table[x] = i


while g.GetNodes():

    v = get_maximum_threshold_node_id()

    if threshold_table[v] > 0:
        v = get_maximum_degree_node_id()
        seed_set.append(v)
        update_nodes(v)

    g.DelNode(v)

    del degree_table[v]
    del threshold_table[v]

print('Seed Set Length: ', len(seed_set))
