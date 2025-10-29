"""Min Stack"""
class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if len(self.stack) > 0:
            minimum = min(self.stack[-1][1], val)
            self.stack.append((val, minimum))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

'''Complexity Analysis:
Time Complexity: O(1)
Space Complexity: O(N)'''

# Testcase
stack1 = MinStack()
stack1.push(-2)
stack1.push(0)
stack1.push(-3)
print(stack1.getMin())
stack1.pop()
print(stack1.top())
print(stack1.getMin())