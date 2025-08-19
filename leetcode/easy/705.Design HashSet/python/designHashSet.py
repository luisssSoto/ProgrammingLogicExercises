"""Design a HashSet"""

# Approach 1: Without Built-in Hash Table Data Structure (set or map)
class MyHashSet:

    def __init__(self):
        self.my_bucket = []

    def add(self, key: int) -> None:
        self.my_bucket.append(key)

    def remove(self, key: int) -> None:
        first_index = matches = 0
        last_index = len(self.my_bucket) - 1
        while first_index <= last_index:
            if self.my_bucket[first_index] == key:
                matches += 1
                while last_index > first_index:
                    if self.my_bucket[last_index] != key:
                        self.my_bucket[first_index], self.my_bucket[last_index] = self.my_bucket[last_index], self.my_bucket[first_index]
                        last_index -= 1
                        break
                    else:
                        matches += 1
                    last_index -= 1
            first_index += 1
        self.my_bucket = self.my_bucket[:len(self.my_bucket) - matches]
        return self.my_bucket
    def contains(self, key: int) -> bool:
        if key in self.my_bucket:
            return True
        else:
            return False

'''Complexity Analysis:
Time Complexity: remove() -> O(N2)
Space Complexity: add() -> O(N)'''

# Approach 2: With a Hash Table Built-in Data Structure (map)
class MyHashSet:

    def __init__(self):
        self.my_bucket = {}

    def add(self, key: int) -> None:
        if key in self.my_bucket:
            self.my_bucket[key].append(key)
        else:
            self.my_bucket[key] = []
            self.my_bucket[key].append(key)

    def remove(self, key: int) -> None:
        if key in self.my_bucket:
            del self.my_bucket[key]

    def contains(self, key: int) -> bool:
        if key in self.my_bucket:
            return True
        else:
            return False
        

'''Complexity Analysis:
Time Complexity: remove() -> O(1)
Space Complexity: add() -> O(N)'''

# Approach 3: Linked List as a Bucket
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)


class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class Bucket:
    def __init__(self):
        # a pseudo head
        self.head = Node(0)

    def insert(self, newValue):
        # if not existed, add the new element to the head.
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            # set the new head.
            self.head.next = newNode

    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # value existed already, do nothing
                return True
            curr = curr.next
        return False
    
'''Complexity Analysis:
Time Complexity: O(N/K)
Space Complexity: O(K + M)'''