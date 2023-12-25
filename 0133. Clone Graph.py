# BFS
# Runtime: O(V+E)
# Space: O(V)

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        # Check for if node is empty, just return None if it is
        if not node:
            return None

        visited = {}
        to_visit = Deque()
        to_visit.append(node)

        # Create a copy of the starting node and add it to visited
        visited[node] = Node(node.val)

        # Loop through the graph
        while to_visit:
            # Get the next node from the to_visit
            cur_node = to_visit.popleft()

            # If current node is not already in visited, add a copy of it
            if cur_node not in visite:
                visited[cur_node] = Node(cur_node.val)

            # Loop through the current node's neighbors
            for neighbor in cur_node.neighbors:
                # If current neighbor is not in visited, create a copy of the neighbor and add it to visited
                if neighbor not in visited:
                    # Create a copy of the neighbor and add it to visited
                    visited[neighbor] = Node(neighbor.val)
                    to_visit.append(neighbor)

                # Add the copy of the neighbor to the copy of the current node's neighbors
                visited[cur_node].neighbors.append(visited[neighbor])

        return visited[node]

