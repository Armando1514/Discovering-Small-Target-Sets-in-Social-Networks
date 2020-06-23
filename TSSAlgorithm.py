import GraphTools

g = GraphTools.load_graph_from_txt("p2p-Gnutella31.txt")
print('Graph Nodes: %d, Edges: %d' % (g.GetNodes(), g.GetEdges()))

g = GraphTools.deferred_decisions_with_uniform_probability(g)
g = GraphTools.constant_threshold_assignment(g, 2)

print('After Deferred decision Nodes: %d, Edges: %d' % (g.GetNodes(), g.GetEdges()))

seed_set = []
nodes_to_remove = True
i = 0
while g.GetNodes() != 0:
    if nodes_to_remove:
        nodes_to_remove = False
        for n in g.Nodes():
            node_threshold = g.GetIntAttrDatN(n.GetId(), "threshold")
            node_in_degree = n.GetInDeg()

            if node_threshold == 0:
                for node_out_id in n.GetOutEdges():
                    node_out_threshold = g.GetIntAttrDatN(node_out_id, "threshold")
                    if node_out_threshold > 0:
                        node_out_threshold = node_out_threshold - 1
                        if node_out_threshold == 0 or g.GetNI(node_out_id).GetInDeg() - 1 < 1:
                            nodes_to_remove = True
                        g.AddIntAttrDatN(node_out_id, node_out_threshold, "threshold")
                g.DelNode(n.GetId())
            elif node_in_degree < node_threshold:
                seed_set.append(n.GetId())
                for node_out_id in n.GetOutEdges():
                    node_out_threshold = g.GetIntAttrDatN(node_out_id, "threshold")
                    node_out_threshold = node_out_threshold - 1
                    if node_out_threshold == 0 or g.GetNI(node_out_id).GetInDeg() - 1 < 1:
                        nodes_to_remove = True
                    g.AddIntAttrDatN(node_out_id, node_out_threshold, "threshold")
                g.DelNode(n.GetId())

    else:

        max_value = -1
        node_max = -1
        for sub_n in g.Nodes():
            node_threshold = g.GetIntAttrDatN(sub_n.GetId(), "threshold")
            node_in_degree = sub_n.GetInDeg()
            if node_threshold > node_in_degree or node_in_degree < 1:
                nodes_to_remove = True
                break
            else:
                node_formula = node_threshold / (node_in_degree * (node_in_degree + 1))
                if node_formula > max_value:
                    max_value = node_formula
                    node_max = sub_n.GetId()
                node_max_object = g.GetNI(node_max)
                for node_max_out_id in node_max_object.GetOutEdges():
                    node_out_threshold = g.GetIntAttrDatN(node_max_out_id, "threshold")
                    node_in_degree = g.GetNI(node_max_out_id).GetInDeg()
                    if node_out_threshold > (node_in_degree - 1) or node_in_degree < 1:
                        nodes_to_remove = True
        if node_max > -1:
            g.DelNode(node_max)


print('Seed Set Length: ', len(seed_set))
print('Seed Set Nodes: ', seed_set)
