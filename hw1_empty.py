# Skeleton file for HW1
# =====================================
# IMPORTANT: You are NOT allowed to modify the method signatures 
# (i.e. the arguments and return types each function takes). 
# We will pass your grade through an autograder which expects a specific format.
# =====================================


# Do not include any other files or an external package, unless it is one of
# [numpy, pandas, scipy, matplotlib, random]
# please contact us before sumission if you want another package approved.
import numpy as np
import matplotlib.pyplot as plt

# Implement the methods in this class as appropriate. Feel free to add other methods
# and attributes as needed. 
class UndirectedGraph:
    def __init__(self,number_of_nodes):
        '''Assume that nodes are represented by indices/integers between 0 and number_of_nodes - 1.'''
        # TODO: Implement this method
        pass
    
    def add_edge(self, nodeA, nodeB):
        ''' Adds an undirected edge to the graph, between nodeA and nodeB. Order of arguments should not matter'''
        # TODO: Implement this method
        pass
    
    def edges_from(self, nodeA):
        ''' This method shold return a list of all the nodes nodeB such that nodeA and nodeB are 
        connected by an edge'''
        # TODO: Implement this method
        pass
    
    def check_edge(self, nodeA, nodeB):
        ''' This method should return true is there is an edge between nodeA and nodeB, and false otherwise'''
        # TODO: Implement this method
        pass
    
    def number_of_nodes(self):
        ''' This method should return the number of nodes in the graph'''
        # TODO: Implement this method
        pass


# Problem 9(a)
def create_graph(n,p):
    ''' Given number of nodes n and probability p, output an UndirectedGraph with n nodes, where each
    pair of nodes is connected by an edge with probability p'''
    # TODO: Implement this method
    pass

# Problem 9(b)
def shortest_path(G,i,j):
    ''' Given an UndirectedGraph G and nodes i,j, output the length of the shortest path between i and j in G.
    If i and j are disconnected, output -1.'''
    # TODO: Implement this method
    pass

# Problem 9(c)
def avg_shortest_path(G, num_samples=1000):
    ''' Given an UndirectedGraph G, return an estimate of the average shortest path in G, where the average is taken
    over all pairs of CONNECTED nodes. The estimate should be taken by sampling num_samples random pairs of connected nodes, 
    and computing the average of their shortest paths. Return a decimal number.'''
    # TODO: Implement this method
    pass

# Problem 10(a)
def create_fb_graph(filename = "facebook_combined.txt"):
    ''' This method should return a undirected version of the facebook graph as an instance of the UndirectedGraph class.
    You may assume that the input graph has 4039 nodes.'''    
    # TODO: Implement this method 
    # for line in open(filename):
    #     pass
    pass

# Please include any additional code you use for analysis, or to generate graphs, here.
# Problem 9(c) if applicable.
# Problem 9(d)
# Problem 10(b)
# Problem 10(c) if applicable.
# Problem 10(d) if applicable.

