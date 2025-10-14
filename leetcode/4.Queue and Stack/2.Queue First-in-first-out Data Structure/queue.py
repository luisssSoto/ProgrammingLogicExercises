"""Queue"""

class MyQueue:
    def __init__(self, size):
        self.size = size
        self.queue = ["available" for _ in range(size)]
        self.head = self.tail = 0

    def enque(self, value):
        if self.tail >= self.size:
            return False
        self.queue[self.tail] = value
        self.tail += 1
        return True
    
    def dequeue(self):
        if self.head >= self.size:
            return False
        self.queue[self.head] = "available"
        self.head += 1
        return True
    
    def get_value(self):
        if self.head >= self.size:
            return False
        return self.queue[self.head]


my_queue = MyQueue(5)
print(my_queue.queue)
print(my_queue.get_value())
my_queue.enque(10)
my_queue.enque(20)
print(my_queue.queue)
print(my_queue.get_value())
print(my_queue.dequeue())
print(my_queue.queue)
my_queue.enque(30)
print(my_queue.queue)
my_queue.enque(40)
my_queue.enque(50)
print(my_queue.queue)
print(my_queue.enque(60))
print(my_queue.get_value())
print(my_queue.dequeue())
print(my_queue.queue)
