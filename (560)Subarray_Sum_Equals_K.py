class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = 0
        curSum = 0
        prefixSum = {0:1}

        for num in nums:
            # add current element to sum
            curSum += num
            # if curSum - k is in hashmap, I would increment the counter with the value corresponding to the key curSum - k. Then I would update the hashmap so that we increment the value of prefixSum[sum]
            if curSum - k in prefixSum:
                counter += prefixSum[curSum - k]

            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        return counter
