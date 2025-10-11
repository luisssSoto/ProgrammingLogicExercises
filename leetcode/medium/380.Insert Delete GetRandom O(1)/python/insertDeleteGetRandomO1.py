"""Insert Delete Get Random O(1)"""

import random
class RandomizedSet:

    def __init__(self): 
        self.unique_values = {}

    def insert(self, val: int) -> bool:
        if val not in self.unique_values:
            self.unique_values[val] = val
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.unique_values:
            self.unique_values.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        random_val = random.choice(list(self.unique_values))
        return self.unique_values[random_val]
    
'''Complexity Analysis:
Time Complexity: O(1)
Space Complexity: O(N)'''