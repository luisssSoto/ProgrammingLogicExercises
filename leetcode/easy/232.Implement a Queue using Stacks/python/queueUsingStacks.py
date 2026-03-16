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