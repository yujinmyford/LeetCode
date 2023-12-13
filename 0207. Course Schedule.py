# DFS
# Runtime: O(V + E), where V is the number of courses and E is the number of dependencies
# Space: O(n)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create adjacency list with prerequisites
        adj = defaultdict(list)
        for a, b in prerequisites:
            if a == b:
                return False
            adj[b].append(a)

        # DFS
        def DFS(cur_node, cur_path, visited, adj_list):
            cur_path.add(cur_node)
            visited.add(cur_node)

            for neighbor in adj_list[cur_node]:
                if cur_node == neighbor:
                    continue
                if neighbor in cur_path:
                    return True
                if neighbor not in visited and DFS(neighbor, cur_path, visited, adj_list):
                    return True
            cur_path.remove(cur_node)
            return False
        

        # to check if there is a cycle
        cycle = False
        visited = set()
        courses = tuple(adj.keys())
        # Call DFS for each course
        for course in courses:
            if course not in visited:
                # If there is a cycle, set cycle to True
                if (DFS(course, set(), visited, adj)):
                    cycle = True

        return (not cycle)
