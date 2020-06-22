import snap
import random

G5 = snap.LoadEdgeList(snap.PNGraph, "p2p-Gnutella31.txt", 0, 1)
print("G5: Nodes %d, Edges %d" % (G5.GetNodes(), G5.GetEdges()))

EdgeToRemove = []
for NI in G5.Nodes():
    for Id in NI.GetOutEdges():
        EdgeProbability = random.random();
        RemoveEdge = random.random();
        if EdgeProbability > RemoveEdge:
            EdgeToRemove.append(Id)
    for RM in EdgeToRemove:
        G5.DelEdge(NI.GetId(), RM)
        EdgeToRemove.remove(RM)

print("G5: Nodes %d, Edges %d" % (G5.GetNodes(), G5.GetEdges()))



