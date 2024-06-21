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

INFINITE_DISTANCE = -1


class Color:
    WHITE = 'WHITE'
    GRAY = 'GRAY'
    BLACK = 'BLACK'


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
            raise ValueError(
                f'At least one of the nodes is out of range. Received: ({nodeA}, {nodeB}). '
                f'Expected values are from 0 to {self._nodes_num}')
        if nodeA == nodeB:
            raise ValueError(f'Received the same node twice: {nodeA}')
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
def create_graph(n: int, p: float):
    """ Given number of nodes n and probability p, output an UndirectedGraph with n nodes, where each
    pair of nodes is connected by an edge with probability p"""
    graph = UndirectedGraph(n)
    # run over all pairs of nodes
    for nodeA in range(n - 1):
        for nodeB in range(nodeA + 1, n):
            if random.random() < p:  # add an edge with probability p
                graph.add_edge(nodeA, nodeB)
    return graph


# Problem 9(b)
def shortest_path(G: UndirectedGraph, i: int, j: int):
    """ Given an UndirectedGraph G and nodes i,j, output the length of the shortest path between nodes i and j in G.
    If i and j are disconnected, output -1."""
    # init
    if i == j:
        return 0

    n = G.number_of_nodes()
    color: dict[int, str] = {}  # used to track which nodes were already visited
    distance: dict[int, int] = {}  # minimal distance from i to each node
    parent: dict[int, int] = {}  # parent of each node in the BFS

    for node in range(n):
        color[node] = Color.WHITE
        distance[node] = INFINITE_DISTANCE
        parent[node] = None

    color[i] = Color.GRAY
    distance[i] = 0

    queue: list[int] = [i]

    # ssearch the shortest path
    while len(queue) > 0:
        node1 = queue.pop(0)
        for node2 in G.edges_from(node1):
            if color[node2] == Color.WHITE:
                color[node2] = Color.GRAY
                distance[node2] = distance[node1] + 1
                parent[node2] = node1
                queue.append(node2)
        color[node1] = Color.BLACK
    return distance[j]


# Problem 9(c)
def avg_shortest_path(G: UndirectedGraph, num_samples: int = 1000):
    """ Given an UndirectedGraph G, return an estimate of the average shortest path in G, where the average is taken
    over all pairs of CONNECTED nodes. The estimate should be taken by sampling num_samples random pairs of connected nodes, 
    and computing the average of their shortest paths. Return a decimal number."""
    n = G.number_of_nodes()
    sum_of_distance = 0
    i = 0
    while i < num_samples:
        node1, node2 = random.sample(range(n), 2)
        shortest_distance = shortest_path(G, node1, node2)
        if shortest_distance <= 0:  # check if pair is connected
            continue
        sum_of_distance += shortest_distance
        i += 1
    return sum_of_distance / num_samples  # average


# Problem 10(a)
def create_fb_graph(filename="facebook_combined.txt"):
    """ This method should return an undirected version of the
    facebook graph as an instance of the UndirectedGraph class.
    You may assume that the input graph has 4039 nodes."""
    fb_G = UndirectedGraph(4039)
    for line in open(filename):
        u, v = line.split(" ")
        fb_G.add_edge(int(u), int(v))
    return fb_G


def question_9c():
    G_9c = create_graph(n=1000, p=0.1)
    print(f"9c answer:{avg_shortest_path(G=G_9c)}")


def question_9d():
    x_probabilities = []
    y_avg_shortest_path = []
    probability_ranges = [[i / 100 for i in range(1, 5)],
                          [i / 100 for i in range(5, 51, 5)]]
    for probability_range in probability_ranges:
        for p in probability_range:
            graph = create_graph(1000, p)
            x_probabilities.append(p)
            y_avg_shortest_path.append(avg_shortest_path(G=graph))
    print(x_probabilities)
    print(y_avg_shortest_path)
    plt.plot(x_probabilities, y_avg_shortest_path)
    plt.xlabel('p')
    plt.ylabel('Average shortest path')
    plt.show()


def question_10b():
    G_fb = create_fb_graph()
    print("10b answer:")
    print(avg_shortest_path(G=G_fb))


def question_10c():
    G_fb = create_fb_graph()
    n = G_fb.number_of_nodes()
    cnt = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if G_fb.check_edge(i, j):
                cnt += 1
    max_num_of_edges = n * (n - 1) / 2
    return cnt / max_num_of_edges


def question_10d():
    G_tp = create_graph(4039, 0.010819963503439287)
    print("10d answer")
    print(avg_shortest_path(G=G_tp))
