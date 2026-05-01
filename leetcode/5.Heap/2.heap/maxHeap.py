"""Max Heap"""

class MaxHeap:
    def __init__(self, heap_size):
        self.heap_size = heap_size
        self.max_heap = [0] * (self.heap_size + 1)
        self.real_size = 0
    
    def add(self, element):
        self.real_size += 1
        if self.real_size > self.heap_size:
            print("There is not more space")
            self.real_size -= 1
            return
        self.max_heap[self.real_size] = element
        index = self.real_size
        parent = index // 2
        while self.max_heap[index] > self.max_heap[parent] and index > 1:
            self.max_heap[parent], self.max_heap[index] = self.max_heap[index], self.max_heap[parent]
            index = parent
            parent = index // 2
    
    def peek(self):
        return self.max_heap[1]
    
    def pop(self):
        if self.real_size < 1:
            print("There is not elements in the Heap")
            return self.real_size
        remove_element = self.max_heap[1]
        self.max_heap[1] = self.max_heap[self.real_size]
        self.real_size -= 1
        index = 1
        while index <= self.real_size // 2:
            left = index * 2
            right = index * 2 + 1
            if self.max_heap[index] < self.max_heap[left] or self.max_heap[index] < self.max_heap[right]:
                if self.max_heap[left] > self.max_heap[right]:
                    self.max_heap[left], self.max_heap[index] = self.max_heap[index], self.max_heap[left]
                    index = left
                else:
                    self.max_heap[right], self.max_heap[index] = self.max_heap[index], self.max_heap[right]
                    index = right
            else:
                break
        return remove_element
    
    def size(self):
        return self.real_size
    
    def __str__(self):
        return str(self.max_heap[1: self.real_size + 1])
    
if __name__ == "__main__":
    max_heap1 = MaxHeap(5)
    max_heap1.add(3)
    max_heap1.add(1)
    max_heap1.add(2)
    print(max_heap1)
    print(max_heap1.peek())
    print(max_heap1.pop())
    print(max_heap1.pop())
    print(max_heap1.pop())
    max_heap1.add(4)
    max_heap1.add(5)
    print(max_heap1)
