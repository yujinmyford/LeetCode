# Hashmap, array
# Runtime: O(1)
# Space: O(n)

class RandomizedSet:
    def __init__(self):
        self.hash = {}
        self.actual = []
    
    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        self.actual.append(val)
        self.hash[val] = len(self.actual) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False
    
        to_delete = self.hash[val]
        if to_delete == len(self.actual) - 1:
            self.actual.pop()
            del self.hash[val]
        else:    
            last_val = self.actual[-1]
            self.actual[to_delete] = last_val
            self.hash[last_val] = to_delete
            self.actual.pop()
            del self.hash[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.actual)
