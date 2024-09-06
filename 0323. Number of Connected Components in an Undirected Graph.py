# Graph, DFS

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        for edge1, edge2 in edges:
            adj[edge1].append(edge2)
            adj[edge2].append(edge1)
        
        visited = set()

        def dfs(ver):
            if ver in visited:
                return
            
            visited.add(ver)
            for nei in adj[ver]:
                dfs(nei)
            
        components = 0

        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
        
        return components



# # Graph, DFS
# # Runtime: O()
# # Space: O()

# class UnionFind:

#     def __init__(self):
#         self.f = {}

#     def findParent(self, x: int) -> int:
#         y = self.f.get(x, x)
#         if x != y:
#             y = self.f[x] = self.findParent(y)
#         return y

#     def union(self, x: int, y: int):

#         self.f[self.findParent(x)] = self.findParent(y)

# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         dsu = UnionFind()
#         for a, b in edges:
#             dsu.union(a, b)
#         return len(set(dsu.findParent(x) for x in range(n)))
    
