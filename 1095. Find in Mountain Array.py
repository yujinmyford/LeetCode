# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Save the length of the mountain array
        length = mountain_arr.length()

        # 1. Find the index of the peak element
        low = 1
        high = length - 2
        while low != high:
            peak = (low + high) // 2
            if mountain_arr.get(peak) < mountain_arr.get(peak + 1):
                low = peak + 1
            else:
                high = peak
        peak = low

        # 2. Binary Search in increasing part of array
        low = 0
        high = peak
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) < target:
                low = test_index + 1
            else:
                high = test_index    
        # Check if the target is present in the strictly increasing part
        if mountain_arr.get(low) == target:
            return low
        
        # 3. Binary Search in decreasing part of array
        low = peak + 1
        high = length - 1
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) > target:
                low = test_index + 1
            else:
                high = test_index
        # Check if the target is present in the strictly decreasing part
        if mountain_arr.get(low) == target:
            return low
        
        # Target is not present in the mountain array
        return -1
