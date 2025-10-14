"""My Circular Queue"""

class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.queue = [None for _ in range(self.size)]
        self.head = self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull() is True:
            return False
        self.queue[self.tail] = value
        self.tail += 1
        if self.tail == self.size:
            self.tail = 0
        return True

    def deQueue(self) -> bool:
        if self.isEmpty() is True:
            return False
        self.queue[self.head] = None
        self.head += 1
        if self.head == self.size:
            self.head = 0
        return True

    def Front(self) -> int:
        if self.isEmpty() is True:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty() is True:
            return -1
        return self.queue[self.tail - 1]

    def isEmpty(self) -> bool:
        if self.head == self.tail and self.queue[self.head] is None:
            return True
        return False

    def isFull(self) -> bool:
        if self.head == self.tail and self.queue[self.tail] is not None:
            return True
        return False