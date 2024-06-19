# Skeleton file for HW1
# =====================================
# IMPORTANT: You are NOT allowed to modify the method signatures 
# (i.e. the arguments and return types each function takes). 
# We will pass your grade through an autograder which expects a specific format.
# =====================================


import random

# Do not include any other files or an external package, unless it is one of
# [numpy, pandas, scipy, matplotlib, random]
# please contact us before submission if you want another package approved.
import matplotlib.pyplot as plt


# Implement the methods in this class as appropriate. Feel free to add other methods
# and attributes as needed. 
class UndirectedGraph:
    def __init__(self, number_of_nodes: int):
        """Assume that nodes are represented by indices/integers between 0 and (number_of_nodes - 1)."""
        self._nodes_num = number_of_nodes
        # graph: is a dictionary,
        # keys are the nodes, 
        # values are set of nodes with edge to key node
        self._adjacency_set = {i: set() for i in range(number_of_nodes)}

    def add_edge(self, nodeA: int, nodeB: int):
        """ Adds an undirected edge to the graph, between nodeA and nodeB. Order of arguments should not matter"""
        if nodeA >= self._nodes_num or nodeB >= self._nodes_num:  # check if nodes exist in graph
            return  # at least one of the nodes is out of range. do nothing
        # add an edge
        self._adjacency_set[nodeA].add(nodeB)
        self._adjacency_set[nodeB].add(nodeA)

    def edges_from(self, nodeA: int):
        """ This method should return a list of all the nodes nodeB such that nodeA and nodeB are
        connected by an edge"""
        return list(self._adjacency_set[nodeA])

    def check_edge(self, nodeA: int, nodeB: int) -> bool:
        """ This method should return true is there is an edge between nodeA and nodeB, and false otherwise"""
        # note: since graph is undirected, if there exists (a,b), there must exist (b, a) - so it's enough to chck one
        return nodeA in self._adjacency_set[nodeB]

    def number_of_nodes(self) -> int:
        """ This method should return the number of nodes in the graph"""
        return self._nodes_num


# Problem 9(a)
def create_graph(n, p):
    ''' Given number of nodes n and probability p, output an UndirectedGraph with n nodes, where each
    pair of nodes is connected by an edge with probability p'''
    G = UndirectedGraph(n)
    # run over all possible edges
    for nodeA in range(n):
        for nodeB in range(nodeA + 1, n):
            if random.random() < p:  # add an edge in probability p
                G.add_edge(nodeA, nodeB)
    return G


# Problem 9(b)
def shortest_path(G, i, j):
    ''' Given an UndirectedGraph G and nodes i,j, output the length of the shortest path between i and j in G.
    If i and j are disconnected, output -1.'''
    n = G.number_of_nodes()
    distance = -1  # distance of the shortest path between i and j
    nodes = [("unvisited", n + 1, None) for t in range(n)]  # list of all nodes attribute,"nodes are index"
    nodes[i] = ("visited", 0, None)  # init starting node
    bfs_queue = [i]  # init queue for the bfs
    while bfs_queue:
        current_node = bfs_queue.pop(0)  # pop the head of the queue
        if current_node == j:  # check if j node is reached
            distance = nodes[j][1]
        neighbors = G.edges_from(current_node)  # get the neighbors
        for neighbor in neighbors:
            if nodes[neighbor][0] == "unvisited":  # check if visited
                nodes[neighbor] = (("visited", nodes[current_node][1] + 1, current_node))  # update attribute
                bfs_queue.append(neighbor)  # add to end of queue
    return distance


# Problem 9(c)
def avg_shortest_path(G, num_samples=1000):
    ''' Given an UndirectedGraph G, return an estimate of the average shortest path in G, where the average is taken
    over all pairs of CONNECTED nodes. The estimate should be taken by sampling num_samples random pairs of connected nodes, 
    and computing the average of their shortest paths. Return a decimal number.'''
    n = G.number_of_nodes()
    sum_of_distance = 0
    i = 0
    while i < num_samples:
        node1 = random.randint(0, n - 1)
        node2 = random.randint(0, n - 1)
        shortest_distance = shortest_path(G, node1, node2)
        if shortest_distance <= 0:  # check if pair is connected
            continue
        sum_of_distance += shortest_distance
        i += 1
    return sum_of_distance / num_samples  # return average


# Problem 10(a)
def create_fb_graph(filename="facebook_combined.txt"):
    ''' This method should return a undirected version of the facebook graph as an instance of the UndirectedGraph class.
    You may assume that the input graph has 4039 nodes.'''
    fb_G = UndirectedGraph(4039)
    for line in open(filename):
        edge = line.split(" ")
        fb_G.add_edge(int(edge[0]), int(edge[1]))
    return fb_G


# Please include any additional code you use for analysis, or to generate graphs, here.
# Problem 9(c) if applicable.
G_9c = create_graph(n=1000, p=0.1)
print("9c answer:")
print(avg_shortest_path(G=G_9c))
# Problem 9(d)
X = []
Y = []
for i in range(1, 5):
    print(i)
    p = i / 100
    G_9d = create_graph(1000, p)
    X.append(p)
    Y.append(avg_shortest_path(G=G_9d))
for i in range(5, 51, 5):
    print(i)
    p = i / 100
    G_9d = create_graph(1000, p)
    X.append(p)
    Y.append(avg_shortest_path(G=G_9d))
print(X)
print(Y)
plt.plot(X, Y)
plt.xlabel('p')
plt.ylabel('Average shortest path')
plt.show()
# Problem 10(b)
G_fb = create_fb_graph()
print("10b answer:")
print(avg_shortest_path(G=G_fb))
# Problem 10(c) if applicable.
G_tp = create_graph(4039, 0.001)
print(avg_shortest_path(G=G_tp))
# Problem 10(d) if applicable.
G_tp = create_graph(4039, 0.0028)
print("10d answer")
print(avg_shortest_path(G=G_tp))
