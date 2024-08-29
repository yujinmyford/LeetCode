class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        visited = set()
        
        def dfs(curr_node):
            if curr_node == destination:
                return True
            if curr_node not in visited:
                visited.add(curr_node)
                for next_node in graph[curr_node]:
                    if dfs(next_node):
                        return True
            return False
            
        return dfs(source)
