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

def dfs_forest_recursive(adj: Dict[Hashable, List[Hashable]]):
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
    cycles = []
    
    time = {
        'time': 0
    }

    for node in adj.keys():
        color[node] = Color.WHITE
        parent[node] = None

    for node in adj.keys():
        if color[node] == Color.WHITE:
            dfs_visit(node, adj, color, parent, discovery_time, finish_time, cycles, time)
    return parent, discovery_time, finish_time, cycles

def dfs_visit(u: Hashable, adj, color, parent, discovery_time, finish_time, cycles, time):
    color[u] = Color.GRAY
    time['time'] += 1
    discovery_time[u] = time['time']
    for v in adj[u]:
        if color[v] == Color.WHITE:
            parent[v] = u
            dfs_visit(v, adj, color, parent, discovery_time, finish_time, cycles, time)
        elif color[v] == Color.GRAY:
            cycle = [v]
            current_node = u
            while current_node != v:
                cycle.insert(0, current_node)
                current_node = parent[current_node]
            cycle.insert(0, v)
            cycles.append(cycle)
                
    color[u] = Color.BLACK
    time['time'] += 1
    finish_time[u] = time['time']

def topological_sort(adj: Dict[Hashable, List[Hashable]]) -> List[Tuple[Hashable, int]]:
    '''
    Returns a topological sort of the nodes in the directed graph.

    There wouldn't be any need to sort items by finish time if we would capture that list
    as the finish time of the nodes are created by the dfs algorithm.
    '''
    _, _, finish_time = dfs_forest(adj)
    return sorted(finish_time.items(), key = lambda x: x[1])

