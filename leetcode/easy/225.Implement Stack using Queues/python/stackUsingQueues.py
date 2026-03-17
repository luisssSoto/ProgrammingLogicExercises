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