"""Two Sum III Data Structure Design"""

class TwoSum:

    def __init__(self):
        self.count_nums = {}

    def add(self, number: int) -> None:
        if number not in self.count_nums:
            self.count_nums[number] = 1
        else:
            self.count_nums[number] += 1

    def find(self, value: int) -> bool:
        for num in self.count_nums.keys():
            complement = value - num
            if complement != num:
                if complement in self.count_nums:
                    return True
            elif self.count_nums[complement] > 1:
                return True
        return False


'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''