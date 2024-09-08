class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        memo = {}

        def max_points(num):
            # Check for base cases
            if num == 0:
                return 0
            if num == 1:
                return points[1]
            if num not in memo:
                memo[num] = max(max_points(num - 1), max_points(num - 2) + points[num])
            
            # Apply recurrence relation
            return memo[num]
        
        return max_points(max_number)
