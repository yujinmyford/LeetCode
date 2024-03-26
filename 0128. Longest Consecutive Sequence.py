class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # initiate hashmap
        collection = {}

        for i in range(len(nums)):
            collection[nums[i]] = nums[i] + 1
        
        max_count = 0   

        # go through keys in collection
        for key in collection.keys():
            cur = key
            count = 1
            # if the element before this one is in collection, already 
            if (cur - 1) not in collection:
                # increment count for as long as consecutive
                while (cur + count) in collection:
                    count += 1
                max_count = max(max_count, count)
        
        return max_count


