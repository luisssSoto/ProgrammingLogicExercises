class MyStack:

    def __init__(self):
        self.stack = [None for x in range(100)]
        self.length = 0

    def push(self, x: int) -> None:
        self.stack[self.length] = x
        self.length += 1

    def pop(self) -> int:
        self.length -= 1
        if self.length >= 0:
            return self.stack[self.length]
        else:
            self.length = 0

    def top(self) -> int:
        return self.stack[self.length - 1]

    def empty(self) -> bool:
        return True if self.length == 0 else False
    
class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        val = self.q1.pop()
        self.q1 = self.q2
        self.q2 = []
        return val

    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return True if len(self.q1) == 0 else False
    
'''Complexity Analysis:
For all the methods:
Time Complexity: O(1)
Space Complexity: O(1)

But for the pop method:
Time Complexity: O(N)
Space Complexity: O(1)
'''