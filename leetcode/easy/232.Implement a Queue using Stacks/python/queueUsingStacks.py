"""Queue Using Stacks"""
# 1. Approach
class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return True if len(self.queue) == 0 else False
    
# 2. Approach
class MyQueue:

    def __init__(self):
        self.queue = [None for x in range(100)]
        self.length = 0

    def push(self, x: int) -> None:
        self.queue[self.length] = x
        self.length += 1
        print(self.queue)

    def peek(self) -> int:
        return self.queue[0]

    def pop(self) -> int:
        val = self.peek()
        for i in range(self.length - 1):
            self.queue[i] = self.queue[i + 1]
        self.length -= 1
        return val

    def empty(self) -> bool:
        return True if self.length == 0 else False
    
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while not self.empty():
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

    def peek(self) -> int:
        return self.s1[-1]

    def pop(self) -> int:
        return self.s1.pop()

    def empty(self) -> bool:
        return True if len(self.s1) == 0 else False
    
'''Complexity Analysis:
For all the methods:
Time Complexity: O(1)
Space Complexity: O(1)

But for the push method:
Time Complexity: O(N)
Space Complexity: O(N)
'''