import operator

import GraphTools

g = GraphTools.load_graph_from_txt("facebook-user-1.txt")
print('Graph Nodes: %d, Edges: %d' % (g.GetNodes(), g.GetEdges()))

g =GraphTools.deferred_decisions_with_uniform_probability(g)

g = GraphTools.constant_threshold_assignment(g, 2)

print('After Deferred decision Nodes: %d, Edges: %d' % (g.GetNodes(), g.GetEdges()))

seed_set = []

formula_table = {}
explored_nodes = []

node_with_threshold_zero = []
node_with_degree_below_threshold = []


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
        if g.GetIntAttrDatN(n_id, "threshold") < 1:
            node_with_threshold_zero.append(n_id)
        elif g.GetIntAttrDatN(n_id, "threshold") > node.GetInDeg():
            node_with_degree_below_threshold.append(n_id)


def update_formula(nodes):
    for node_id in nodes:
        if g.IsNode(node_id):
            n = g.GetNI(node_id)
            n_threshold = g.GetIntAttrDatN(node_id, "threshold")
            n_in_degree = n.GetInDeg()
            node_formula = n_threshold / (n_in_degree * (n_in_degree + 1))
            formula_table[node_id] = node_formula


def threshold_reached(n_id):
    node_references = g.GetNI(n_id)
    id_node_where_update_formula = []
    for node_out in node_references.GetOutEdges():
        node_out_threshold = g.GetIntAttrDatN(node_out, "threshold")
        if node_out_threshold > 0:
            node_out_threshold = node_out_threshold - 1
        g.AddIntAttrDatN(node_out, node_out_threshold, "threshold")
        if node_out_threshold == 0:
            if node_out in node_with_degree_below_threshold:
                node_with_degree_below_threshold.remove(node_out)
            node_with_threshold_zero.append(node_out)
        elif (g.GetNI(node_out).GetInDeg() - 1) < node_out_threshold:
            node_with_degree_below_threshold.append(node_out)
        else:
            id_node_where_update_formula.append(node_out)

    g.DelNode(n_id)
    update_formula(id_node_where_update_formula)
    del formula_table[n_id]


def degree_below_threshold(n_id):
    seed_set.append(n_id)
    node_references = g.GetNI(n_id)
    id_node_where_update_formula = [n]
    for node_out in node_references.GetOutEdges():
        node_out_threshold = g.GetIntAttrDatN(node_out, "threshold")
        if node_out_threshold > 0:
            node_out_threshold = node_out_threshold - 1
        g.AddIntAttrDatN(node_out, node_out_threshold, "threshold")
        if node_out_threshold == 0:
            if node_out in node_with_degree_below_threshold:
                node_with_degree_below_threshold.remove(node_out)
            node_with_threshold_zero.append(node_out)
        elif (g.GetNI(node_out).GetInDeg() - 1) < node_out_threshold:
            node_with_degree_below_threshold.append(node_out)
        else:
            id_node_where_update_formula.append(node_out)
    g.DelNode(n_id)
    update_formula(id_node_where_update_formula)
    del formula_table[n_id]


def get_maximum_node_id():
    return max(formula_table.items(), key=operator.itemgetter(1))[0]


def choose_the_maximum_ratio(n_id):
    node_references = g.GetNI(n_id)
    id_node_where_update_formula = []

    for node_out in node_references.GetOutEdges():
        if (g.GetNI(node_out).GetInDeg() - 1) < g.GetIntAttrDatN(node_out, "threshold"):
            node_with_degree_below_threshold.append(node_out)
        else:
            id_node_where_update_formula.append(node_out)

    g.DelNode(n_id)
    update_formula(id_node_where_update_formula)
    del formula_table[n_id]


calculate_formula()

while g.GetNodes():

    if len(node_with_threshold_zero) > 0:
        n = node_with_threshold_zero.pop()
        if g.IsNode(n):
            threshold_reached(n)
    elif len(node_with_degree_below_threshold) > 0:
        n = node_with_degree_below_threshold.pop()
        if g.IsNode(n) and not n in seed_set:
            degree_below_threshold(n)
    else:
        n = get_maximum_node_id()

        if g.IsNode(n):
            choose_the_maximum_ratio(n)

print('Seed Set Length: ', len(seed_set))


