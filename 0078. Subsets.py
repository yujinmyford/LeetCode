# Runtime: O(N)
# Space: O(N)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            # Out of bounds, base case, so append current subset to res and return
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i], left of pyramid
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i], right of pyramid
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
