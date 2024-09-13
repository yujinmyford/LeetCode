# Runtime: O(n^2)
# Space: O(n)

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        minSize = float('inf')

        visited = set()

        for x1, y1 in points:
            for x2, y2 in visited:
                # Means we can form rectangle
                if (x1, y2) in visited and (x2, y1) in visited:
                    size = abs(x2 - x1) * abs(y2 - y1)
                    minSize = min(minSize, size)
        
            visited.add((x1, y1))
        
        return minSize if minSize != float('inf') else 0
