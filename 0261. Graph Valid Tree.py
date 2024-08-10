# Graph, DFS
# Runtime: O(V+E)
# Space: O(V+E)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Automatically return true if empty
        if not n:
            return True
        
        # Create adjacenty list 
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i: int, prev: int) -> bool:
            # If visted already means loop, return False
            if i in visit:
                return False

            # Add current node to visit
            visit.add(i)
            for j in adj[i]:
                # To ensure we don't go back to previous node, cause false loop
                if j == prev:
                    continue
                # Ensure all children are valid
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)
    
