import snap
import random


def load_graph_from_txt(txt):
    g = snap.LoadEdgeList(snap.PNGraph, txt, 0, 1)
    return g


def deferred_decisions_with_uniform_probability(g):
    edge_to_remove = []
    for n in g.Nodes():
        for edge_id in n.GetOutEdges():
            edge_probability = random.random()
            remove_edge_probability = random.random()
            if edge_probability > remove_edge_probability:
                edge_to_remove.append(edge_id)
        for rm in edge_to_remove:
            g.DelEdge(n.GetId(), rm)
            edge_to_remove.remove(rm)
    return g


def deferred_decisions_with_proportional_to_the_degree(g):
    edge_to_remove = []
    for n in g.Nodes():
        for edge_id in n.GetOutEdges():
            edge_probability = 1 / n.GetDeg()
            remove_edge_probability = random.random()
            if edge_probability > remove_edge_probability:
                edge_to_remove.append(edge_id)
        for rm in edge_to_remove:
            g.DelEdge(n.GetId(), rm)
            edge_to_remove.remove(rm)
    return g


def constant_threshold_assignment(g, constant_value):
    g = snap.ConvertGraph(snap.PNEANet, g)
    for n in g.Nodes():
        g.AddIntAttrDatN(n.GetId(), constant_value, "threshold")
    return g


def proportional_to_the_degree_threshold_assignment(g):
    g = snap.ConvertGraph(snap.PNEANet, g)
    for n in g.Nodes():
        g.AddIntAttrDatN(n.GetId(), n.GetDeg(), "threshold")
    return g


def proportional_to_the_out_degree_threshold_assignment(g):
    g = snap.ConvertGraph(snap.PNEANet, g)
    for n in g.Nodes():
        g.AddIntAttrDatN(n.GetId(), n.GetOutDeg(), "threshold")
    return g


def proportional_to_the_in_degree_threshold_assignment(g):
    g = snap.ConvertGraph(snap.PNEANet, g)
    for n in g.Nodes():
        g.AddIntAttrDatN(n.GetId(), n.GetInDeg(), "threshold")
    return g