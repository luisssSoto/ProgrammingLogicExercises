"""Moving Average from Data Stream"""

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = [0 for _ in range(self.size)]
        self.elements = 0
        self.tail = 0

    def next(self, val: int) -> float:
        self.tail = self.elements % self.size
        self.elements += 1
        self.queue[self.tail] = val
        return sum(self.queue) / min(self.elements, self.size)
    
'''Complexity Analysis:
Time Complexity: O(1)
Space Complexity: O(N)'''