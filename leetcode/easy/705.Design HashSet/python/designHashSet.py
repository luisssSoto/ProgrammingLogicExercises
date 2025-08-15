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