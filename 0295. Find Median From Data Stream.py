# Heap
# Runtime: O(log n)
# Space: O(n)

import heapq

class MedianFinder:


    def __init__(self):
        # Initialize left and right heap
        # Left is max heap representing left half of stream, right is min heap representing right half of stream
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        # If num we're trying to add is less than or equal to largest element in left, we add to left
        if not self.left or num <= -self.left[0]:
            # Add negative numbers to make max heap
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        # If the difference in length between left and right is larger than 1,  means we have to rebalance
        if abs(len(self.left) - len(self.right)) > 1:
            # If left half is larger pop from left and push to right
            if len(self.left) > len(self.right):
                temp = -heapq.heappop(self.left)
                heapq.heappush(self.right, temp)
            else:
                temp = heapq.heappop(self.right)
                heapq.heappush(self.left, -temp)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.left) < len(self.right):
            return self.right[0]
        # If length of stream is even get first in max and min heap and add together then divide by 2 for median
        else:
            return (-self.left[0] + self.right[0]) / 2


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
