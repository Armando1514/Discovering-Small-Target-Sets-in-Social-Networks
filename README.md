# Discovering Small Target Sets in Social Networks


<p align="center">
  <img src="https://ferrara.link/img/Discovering-Small-Target%20Sets-in-Social-Networks/social-network-analysis.png">
</p>

Study about the algorithm for discovering small target sets in social networks presented in this [paper](https://link.springer.com/article/10.1007/s00453-017-0390-5) . In the document the algorithm is presented for non-directed graphs, the purpose of this investigation is to present the algorithm for directed graphs and show some results to see how the algorithm performs.

**Problem** : Given a network represented by a graph G=(V, E), we consider a dynamical process of influence diffusion in G that evolves as follows: Initially only the nodes of a given S⊆ V are influenced; subsequently, at each round, the set of influenced nodes is augmented by all the nodes in the network that have a sufficiently large number of already influenced neighbors. The question is to determine a small subset of nodes S(a target set) that can influence the whole network. This is a widely studied problem that abstracts many phenomena in the social, economic, biological, and physical sciences. It is known that the above optimization problem is hard to approximate.

We describe below the main steps of the algorithm given as input a graph G = (V, E): :

1. **Pre-processing phase**:
   1. To the graph G we apply the **[principle of deferred decisions](https://en.wikipedia.org/wiki/Principle_of_deferred_decision)** through the various methods, one of these, is to launch at the beginning for each edge the coin and memorize only the edges that are successful. Why? In a social network, it is not supposed that every one of my friends will affect my choices, there will be some who have no influence on me, so we generate this case by this principle
   2. For each node in G, we assign a threshold, which describes how many adjacent nodes need to be activated (activated does it means that they adopt a product or a behavior), to influence the node choices

2. **Algorithm for selecting small target sets**:
   1. If there is a node v that has a threshold  0,  decrease by 1 the threshold of the nodes to which the outgoing arcs of v refer, eliminate the node v (consequently even the edges of v). Repeat the cycle starting from this point again. If v doesn't exist, then go to step 2.
   2. If there exists a node v whose threshold is less than the entering edges, add it to the solution set and decrease by 1 the threshold of the nodes to which the outgoing edges of v refer, eliminate the node v (consequently even the edges of v). This because it will not be influenced by the nodes that have an entering edge in it, even if these nodes are active, the threshold would still be greater. Repeat the cycle starting from point 1. If v does not exist, go to point 3.
   3. Take the node v that maximize this value: **k (u) \ [(d_in (u)) * (d_in (u) + 1)]**, where k (u) is the threshold of u, while d_in (u) is the degree of the edges entering in u. This heuristic is directly proportional to its remaining threshold and inversely proportional to its degree. The node is eliminated, and it must be influenced by its neighbors. After that, Go to step 1.

Generally, the algorithm performs better than a greedy algorithm that takes each time the node that has a threshold greater than 0, and that has a degree of the outgoing edges greater than all the others in the graph (therefore its choice will affect more nodes). Here we show some results, showing the cardinality of the solution set using the two algorithms (The reference datasets are in this repository). 
Note that the proposed algorithm has a lower cardinality than the greedy one. So with fewer nodes, affect the whole set.

Results with the dataset  "[facebook-user-1.txt](https://github.com/Armando1514/Discovering-Small-Target-Sets-in-Social-Networks/blob/master/facebook-user-1.txt)" :

![img](https://ferrara.link/img/Discovering-Small-Target%20Sets-in-Social-Networks/image1.png)

Results with the dataset "[facebook-users.txt](https://github.com/Armando1514/Discovering-Small-Target-Sets-in-Social-Networks/blob/master/facebook-users.txt)" :

![img](https://ferrara.link/img/Discovering-Small-Target%20Sets-in-Social-Networks/image1.png)

### Credits

- [Snap-Stanford library](https://snap.stanford.edu/)
- [Dataset](https://snap.stanford.edu/data/ego-Facebook.html)
- [Social Circles In Ego Networks](http://i.stanford.edu/~julian/pdfs/nips2012.pdf)
- [Discovering Small Target Sets in Social Networks: A Fast and Effective Algorithm](https://link.springer.com/article/10.1007/s00453-017-0390-5)

