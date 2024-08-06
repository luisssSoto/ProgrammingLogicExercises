"""Queue - Implementation"""

'''
To implement a queue, we may use a dynamic array and an index 
pointing to the head of the queue.

As mentioned, a queue should support two operations: enqueue and 
dequeue. Enqueue appends a new element to the queue while dequeue 
removes the first element. So we need an index to indicate the 
starting point.

Here is an implementation for your reference:

Drawback
The implementation above is straightforward but is inefficient in some 
cases. With the movement of the start pointer, more and more space is 
wasted. And it will be unacceptable when we only have a space limitation.

Let's consider a situation when we are only able to allocate an array 
whose maximum length is 5. Our solution works well when we have only 
added less than 5 elements. For example, if we only called the enqueue 
function four times and we want to enqueue an element 10, we will succeed.

And it is reasonable that we can not accept more enqueue request because
 the queue is full now. But what if we dequeue an element? 

Actually, we should be able to accept one more element in this case.'''

class QueueError(IndexError):
    def __init__(self):
        IndexError.__init__(self)
    
class Queue(QueueError):
    def __init__(self):
        QueueError.__init__(self)
        self.__queue = []

    # enQueue
    def en_queue(self, element):
        self.__element = element
        self.__queue.insert(0, self.__element)
    
    # deQueue
    def de_queue(self):
        if len(self.__queue) != 0:
            del self.__queue[-1]
        else:
            raise QueueError

    # get the front/head item from the queue
    def get_front_element(self):
        return self.__queue[-1]
    
    # check whether the queue is empty or not
    def is_empty(self):
        if len(self.__queue) == 0: return True
        else: return False

    # show queue
    def show_queue(self):
        return self.__queue

queue1 = Queue()
print(queue1)
print(queue1.show_queue())
for i in range(5):
    queue1.en_queue(i)
print(queue1.show_queue())
queue1.de_queue()
print(queue1.show_queue())
print(queue1.get_front_element())
print(queue1.is_empty())
print(queue1.show_queue())

try:
    for i in range(5):
        queue1.de_queue()
except QueueError as e:
    print(e.args)

print('continue')



