from typing import Hashable, List, Dict, Tuple
from enum import Enum

class Color(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3

def dfs_forest(adj : Dict[Hashable, List[Hashable]]) :
    '''
    Assumes that all nodes of the graph are present in `adj`, even if they
    have no children.

    - Returns:
        - parent: Dict[Hashable, Hashable]
        - discovery_time: Dict[Hashable, int]
        - finish_time: Dict[Hashable, int]

    '''
    #1. Initialization of datastructures
    color = {}
    parent = {}
    discovery_time = {}
    finish_time = {}

    for node in adj.keys():
        color[node] = Color.WHITE
        parent[node] = None
    
    stack = []
    time = 0
    for node in adj.keys():
        if color[node] == Color.WHITE:
            time += 1
            discovery_time[node] = time
            color[node] = Color.GRAY
            stack.append(node)

            while len(stack) > 0:
                v = stack[-1]
                all_neighborhood_discovered = True
                if color[v] == Color.GRAY:
                    for child in adj[v]:
                        if color[child] == Color.WHITE:
                            time += 1
                            discovery_time[child] = time
                            color[child] = Color.GRAY
                            parent[child] = v
                            stack.append(child)
                            all_neighborhood_discovered = False
                if all_neighborhood_discovered:
                    stack.pop()
                    time += 1
                    finish_time[v] = time
                    color[v] = Color.BLACK
    
    return parent, discovery_time, finish_time

