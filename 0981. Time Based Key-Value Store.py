# Hashmap (Separate Chaining)
# Runtime: O(log n)
# Space: O(n)

class TimeMap:
    
    def __init__(self):
        # initialize hashmap
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the value to key with value as a list of value and timestamp
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        to_return = ""
        # Store the values in a variable
        values = self.hashmap[key]

        # Use binary search to go through timestamp values
        low = 0
        high = len(values) - 1
        while low <= high:
            mid = (low + high) // 2
            
            # If equal or less than timestamp, we keep this one since we want to return exact value or closest but less than timestamp
            if values[mid][1] <= timestamp:
                to_return = values[mid][0]
                low = mid + 1
            else: 
                high = mid - 1

        return to_return


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
