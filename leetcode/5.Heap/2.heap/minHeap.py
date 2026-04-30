"""Min Heap """

class MinHeap:
    def __init__(self, heap_size):
        self.heap_size = heap_size
        self.min_heap = [0] * (self.heap_size + 1)
        self.real_size = 0

    def add(self, element):
        self.real_size += 1
        if self.real_size > self.heap_size:
            print("Added to many elements")
            self.real_size -= 1
            return
        self.min_heap[self.real_size] = element
        index = self.real_size
        parent = index // 2
        while self.min_heap[index] < self.min_heap[parent] and index > 1:
            self.min_heap[parent], self.min_heap[index] = self.min_heap[index], self.min_heap[parent]
            index = parent 
            parent = index // 2
    
    def peek(self):
        return self.min_heap[1]
    
    def pop(self):
        if self.real_size < 1:
            print("There is not elements in the Heap")
            return self.real_size
        remove_element = self.min_heap[1]
        self.min_heap[1] = self.min_heap[self.real_size]
        self.real_size -=1
        index = 1
        while index <= self.real_size // 2:
            left = index * 2
            right = index * 2 + 1
            if self.min_heap[index] > self.min_heap[left] or self.min_heap[index] > self.min_heap[right]:
                if self.min_heap[left] < self.min_heap[right]:
                    self.min_heap[left], self.min_heap[index] = self.min_heap[index], self.min_heap[left]
                    index = left
                else:
                    self.min_heap[right], self.min_heap[index] = self.min_heap[index], self.min_heap[right]
                    index = right
            else:
                break
        return remove_element 
    
    def size(self):
        return self.real_size
    
    def __str__(self):
        return str(self.min_heap[1 : self.real_size + 1])


if __name__ == "__main__":
    min_heap1 = MinHeap(5)
    min_heap1.add(3)
    min_heap1.add(1)
    min_heap1.add(2)
    print(min_heap1)
    print(min_heap1.peek())
    print(min_heap1.pop())
    print(min_heap1.pop())
    print(min_heap1.pop())
    min_heap1.add(4)
    min_heap1.add(5)
    print(min_heap1)
