import operator

import GraphTools

g = GraphTools.load_graph_from_txt("p2p-Gnutella31.txt")
print('Graph Nodes: %d, Edges: %d' % (g.GetNodes(), g.GetEdges()))

g = GraphTools.deferred_decisions_with_uniform_probability(g)

g = GraphTools.constant_threshold_assignment(g, 2)

print('After Deferred decision Nodes: %d, Edges: %d' % (g.GetNodes(), g.GetEdges()))

seed_set = []

formula_table = {}


def calculate_formula():
    for node in g.Nodes():
        n_id = node.GetId()
        n_threshold = g.GetIntAttrDatN(n_id, "threshold")
        n_in_degree = node.GetInDeg()
        if n_in_degree > 0:
            node_formula = n_threshold / (n_in_degree * (n_in_degree + 1))
            formula_table[n_id] = node_formula
        else:
            formula_table[n_id] = 0


def update_formula(nodes):
    for node_id in nodes:
        if g.IsNode(node_id):
            n = g.GetNI(node_id)
            n_threshold = g.GetIntAttrDatN(node_id, "threshold")
            n_in_degree = n.GetInDeg()
            if n_in_degree > 0:
                node_formula = n_threshold / (n_in_degree * (n_in_degree + 1))
                formula_table[node_id] = node_formula


def threshold_reached(node_id):
    id_node_where_update_formula = []
    node_with_threshold_to_zero = [node_id]
    node_with_degree_below_threshold = []

    while len(node_with_threshold_to_zero) > 0:
        node_to_analyse = node_with_threshold_to_zero.pop()
        n = g.GetNI(node_to_analyse)

        for node_out_id in n.GetOutEdges():
            id_node_where_update_formula.append(node_out_id)
            node_out_threshold = g.GetIntAttrDatN(node_out_id, "threshold")

            if node_out_threshold > 0:
                node_out_threshold = node_out_threshold - 1
                g.AddIntAttrDatN(node_out_id, node_out_threshold, "threshold")
                if g.GetNI(node_out_id).GetInDeg() - 1 < node_out_threshold:
                    node_with_degree_below_threshold.append(node_out_id)
            else:
                node_with_threshold_to_zero.append(node_out_id)

    while len(node_with_degree_below_threshold) > 0:
        node_pop = node_with_degree_below_threshold.pop()
        if g.IsNode(node_pop):
            degree_below_threshold(node_pop)

    g.DelNode(node_id)
    del formula_table[node_id]
    update_formula(id_node_where_update_formula)


def degree_below_threshold(node_id):

    seed_set.append(node_id)
    id_node_where_update_formula = []
    node_with_degree_below_to_zero = [node_id]

    while len(node_with_degree_below_to_zero) > 0:
        node_to_analyse = node_with_degree_below_to_zero.pop()
        if g.IsNode(node_to_analyse):
            n = g.GetNI(node_to_analyse)
            for node_out_id in n.GetOutEdges():

                id_node_where_update_formula.append(node_out_id)
                node_out_threshold = g.GetIntAttrDatN(node_out_id, "threshold")
                node_out_threshold = node_out_threshold - 1
                g.AddIntAttrDatN(node_out_id, node_out_threshold, "threshold")
                if node_out_threshold == 0:
                    threshold_reached(node_out_id)
                elif g.GetNI(node_out_id).GetInDeg() - 1 < node_out_threshold:
                    node_with_degree_below_to_zero.append(node_out_id)
        if g.IsNode(node_id):
            g.DelNode(node_id)
            del formula_table[node_id]
            update_formula(id_node_where_update_formula)


def get_maximum_node_id():
    return max(formula_table.items(), key=operator.itemgetter(1))[0]


def choose_the_maximum_ratio():
    node_id = get_maximum_node_id()
    if g.IsNode(node_id):
        max_node = g.GetNI(node_id)
        id_node_where_update_formula = []
        for node_max_out_id in max_node.GetOutEdges():
            id_node_where_update_formula.append(node_max_out_id)
            update_formula(id_node_where_update_formula)


    if g.IsNode(node_id):
       g.DelNode(node_id)
       del formula_table[node_id]





calculate_formula()
while g.GetNodes() != 0:

    n = g.BegNI()
    node_threshold = g.GetIntAttrDatN(n.GetId(), "threshold")
    node_in_degree = n.GetInDeg()
    if node_threshold == 0:
        threshold_reached(n)
    elif node_in_degree < node_threshold:
        degree_below_threshold(n.GetId())
    else:
        choose_the_maximum_ratio()

print('Seed Set Length: ', len(seed_set))
print('Seed Set Nodes: ', seed_set)
