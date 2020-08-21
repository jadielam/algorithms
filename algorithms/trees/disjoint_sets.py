'''
For a sequence of m operations of type:

a) make_set
b) union
c) find_set

of which n operations as of type make_set
the running time is: O(m * a(n)), where a(n) is a 
very slowly growing function (a(n) <= 4 for all 
practical purposes)
'''
from typing import Hashable

class DisjointSets:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def make_set(self, x: Hashable):
        self.parent[x] = x
        self.rank[x] = 0
    
    def link(self, x: Hashable, y: Hashable):
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
    
    def union(self, x: Hashable, y: Hashable):
        self.link(self.find_set(x), self.find_set(y))
    
    def find_set(self, x: Hashable):    
        path_to_root = []
        y = x
        while y != self.parent[y]:
            path_to_root.append(y)
            y = self.parent[y]
        for a in path_to_root:
            self.parent[a] = y
        return y