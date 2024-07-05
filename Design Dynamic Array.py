class DynamicArray:
    
    # Initialize empty array with capacity > 0
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity

    # Return element at i index
    def get(self, i: int) -> int:
        if i < self.length:
            return self.arr[i]

    # Set the element at index i to n
    def set(self, i: int, n: int) -> None:
        if i < self.length:
            self.arr[i] = n

    # Push the element n to the end of the array
    def pushback(self, n: int) -> None:
        # If array is full, resize
        if self.length == self.capacity:
            self.resize()
            
        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1


    # Pop and return the element at the end of the array
    def popback(self) -> int:
        if self.length > 0:
            end = self.arr[self.length - 1]
            self.length -= 1
            return end

    # Double the capacity of the array
    def resize(self) -> None:
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity 
        
        # Copy elements to newArr
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr

    # Return the number of elements in the array
    def getSize(self) -> int:
        return self.length
    
    # Return the capacity of the array
    def getCapacity(self) -> int:
        return self.capacity
