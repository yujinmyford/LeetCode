# Graph, DFS
# Runtime: O(V + E), where V is the number of courses and E is the number of dependencies
# Space: O(n)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # value is list of prereqs
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            # run dfs on all prereqs
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            # already visited, so remove from set
            visiting.remove(crs)
            # already proven true, so remove prereqs to return true faster next time
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
