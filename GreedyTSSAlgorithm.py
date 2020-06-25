import GraphTools

g = GraphTools.load_graph_from_txt("Slashdot0902.txt")
print('Graph Nodes: %d, Edges: %d' % (g.GetNodes(), g.GetEdges()))

g =GraphTools.deferred_decisions_with_uniform_probability(g)

g = GraphTools.constant_threshold_assignment(g, 2)

print('After Deferred decision Nodes: %d, Edges: %d' % (g.GetNodes(), g.GetEdges()))

seed_set = []

nodes_table = {}


def calculate_tables():
    for node in g.Nodes():
        n_id = node.GetId()
        n_threshold = g.GetIntAttrDatN(n_id, "threshold")
        n_out_degree = node.GetOutDeg()
        nodes_table[n_id] = {"degree": n_out_degree, "threshold": n_threshold}


def get_maximum_degree_node_id():
    max_value = -1
    max_node_id = 0
    for node in nodes_table:
        if nodes_table[node]["threshold"] > 0 and nodes_table[node]["degree"] > max_value:
            max_value = nodes_table[node]["degree"]
            max_node_id = node

    return max_node_id


def get_maximum_threshold_node_id():
    max_node_id = -1
    for node in nodes_table:
        if nodes_table[node]["threshold"] > 0:
            max_node_id = node
            break

    if max_node_id == -1:
        return next(iter(nodes_table))

    return max_node_id


calculate_tables()


def update_nodes(x):
    for out_node in g.GetNI(x).GetOutEdges():

        if nodes_table[out_node]["degree"] > 0 and g.IsEdge(out_node, x):
            nodes_table[out_node]["degree"] = nodes_table[out_node]["degree"] - 1

        if nodes_table[out_node]["threshold"] > 0:
            nodes_table[out_node]["threshold"] = nodes_table[out_node]["threshold"] - 1


while g.GetNodes():

    v = get_maximum_threshold_node_id()
    if nodes_table[v]["threshold"] > 0:
        v = get_maximum_degree_node_id()
        seed_set.append(v)

    update_nodes(v)
    g.DelNode(v)

    del nodes_table[v]

print('Seed Set Length: ', len(seed_set))
print("Seed Set:", seed_set)
