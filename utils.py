# Import librairies
import networkx as nx
import numpy as np
from tqdm import tqdm
def preferential_attachement(graph):
    PA = {}
    N = {node: graph.degree(node) for node in graph.nodes()}
    # Compute similarity metric between any two non-edges nodes
    non_edges = list(nx.non_edges(graph))
    for u, v in tqdm(non_edges):
        PA[(u, v)] = N[u]*N[v]
    return PA
    
def Jaccard(graph):
    Jaccard = {}
    # get the neighbors of each node
    neighbors = {node: set(graph.neighbors(node)) for node in graph.nodes()}
    # Compute similarity metric between any two non-edges nodes
    non_edges = list(nx.non_edges(graph))
    for u, v in tqdm(non_edges):
        # Get the intersection and union of the neighbors of u and v
        inter = len(neighbors[u].intersection(neighbors[v]))
        union = len(neighbors[u].union(neighbors[v]))
        # Compute the Jaccard coefficient
        Jaccard[(u, v)] = inter/union    
    return Jaccard

def AdamicAdar(graph):
    AdamicAdar = {}
    # Get neighbords of each node
    neighbors = {node: set(graph.neighbors(node)) for node in graph.nodes()}
    # Compute similarity metric between any two non-edges nodes
    non_edges = list(nx.non_edges(graph))
    for u, v in tqdm(non_edges):
        # Compute the Adamic/Adar coefficient
        AdamicAdar[(u, v)] = 0
        for z in neighbors[u].intersection(neighbors[v]):
            AdamicAdar[(u, v)] += 1/np.log(graph.degree(z))
        # Compute the Jaccard coefficient    
    return AdamicAdar

