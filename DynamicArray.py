class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity
            
    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:

        if self.length == self.capacity :
            self.resize()
        self.arr[self.length] = n
        self.length = self.length + 1

    def popback(self) -> int:
        valueForReturn = self.arr[self.length-1]
        self.arr[self.length-1] = 0
        self.length -= 1
        return valueForReturn 
 

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        self.arr = self.arr + [0] * (new_capacity - self.capacity)
        self.capacity = new_capacity

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
    

def main():
    arr = DynamicArray(1)

    print("Initial capacity:", arr.getCapacity())  # Output: 1
    print("Initial size:", arr.getSize())          # Output: 0

    arr.pushback(10)
    print("After pushback(10):")
    print("Size:", arr.getSize())                  # Output: 1
    print("Capacity:", arr.getCapacity())          # Output: 1

    arr.pushback(20)  # This should trigger resize
    print("After pushback(20):")
    print("Size:", arr.getSize())                  # Output: 2
    print("Capacity:", arr.getCapacity())          # Output: 2

    print("Get index 1:", arr.get(1))              # Output: 20

    arr.set(1, 25)
    print("After set(1, 25), get index 1:", arr.get(1))  # Output: 25

    popped = arr.popback()
    print("Popped value:", popped)                 # Output: 25
    print("Size after pop:", arr.getSize())        # Output: 1

if __name__ == "__main__":
    main()
