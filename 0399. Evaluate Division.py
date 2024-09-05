# Graph, BFS
# Runtime: O(N * (E + V))
# Space: O(E + V)

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)

        for i, eq in enumerate(equations):
            first, second = eq
            adj[first].append([second, values[i]])
            adj[second].append([first, 1 / values[i]])
        
        def bfs(source, target):
            if source not in adj or target not in adj:
                return -1
            q = deque()
            visited = set()
            q.append([source, 1])
            visited.add(source)
            while q:
                node, weight = q.popleft()

                if node == target:
                    return weight

                for neighbor, neiWeight in adj[node]:
                    if neighbor not in visited:
                        q.append([neighbor, weight * neiWeight])
                        visited.add(neighbor)
            return -1
        
        res = []
        for q in queries:
            res.append(bfs(q[0], q[1]))
        
        return res
