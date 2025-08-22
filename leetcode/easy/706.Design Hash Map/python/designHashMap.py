"""Design Hash Map"""

# class MyHashMap:

#     def __init__(self):
        

#     def put(self, key: int, value: int) -> None:
        

#     def get(self, key: int) -> int:
        

#     def remove(self, key: int) -> None:

class MyKeyValPair:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyBucket:
    def __init__(self):
        self.head = MyKeyValPair(None, None)
    def get_last(self):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        return curr
    def get(self, key):
        curr = self.head.next
        while curr.key != key:
            curr = curr.next
        return curr
    def delete(self, key):
        curr = self.head
        while curr.next.key != key:
            curr = curr.next
        curr.next = curr.next.next
    def show(self):
        curr = self.head
        print(f"curr: {curr}")
        while curr is not None:
            print(f"curr: {curr}, key: {curr.key}, val: {curr.val}, next: {curr.next}")
            curr = curr.next
    

class MyHashMap:
    def __init__(self):
        self.arr = [MyBucket() for x in range(769)]
    def hash_fun(self, key):
        return key % 769
    def exist(self, key, bucket):
        head = bucket.head.next
        while head is not None:
            if head.key == key:
                return True
            head = head.next
        return False
    def get_node(self, key):
        index = self.hash_fun(key)
        right_bucket = self.arr[index]
        curr = right_bucket.head.next
        while curr.key != key:
            curr = curr.next
        return curr
    def put(self, key, val):
        index = self.hash_fun(key)
        right_bucket = self.arr[index]
        if self.exist(key, right_bucket) is True:
            ele = self.get_node(key)
            ele.val = val
        else:
            prev = right_bucket.get_last()
            key_val_obj = MyKeyValPair(key, val)
            temp = prev.next
            prev.next = key_val_obj
            key_val_obj.next = temp
    def get(self, key):
        index = self.hash_fun(key)
        right_bucket = self.arr[index]
        if self.exist(key, right_bucket):
            return right_bucket.get(key).val
        else: 
            return -1
    def remove(self, key):
        index = self.hash_fun(key)
        right_bucket = self.arr[index]
        if self.exist(key, right_bucket) is True:
            right_bucket.delete(key)
        else:
            return None
    def show_items(self, key):
        index = self.hash_fun(key)
        right_bucket = self.arr[index]
        if self.exist(key, right_bucket) is True:
            right_bucket.show()
        else:
            return False


# Testcases: 
my_hash_map = MyHashMap()
my_hash_map.put(1,1)
my_hash_map.put(2,2)
print(my_hash_map.get(1))
print(my_hash_map.get(3))
my_hash_map.put(2,1)
print(my_hash_map.get(2))
my_hash_map.remove(2)
print(my_hash_map.get(2))

'''Complexity Analysis:
Time Complexity: O(N/K)
Space Complexity: O(K + M)
'''