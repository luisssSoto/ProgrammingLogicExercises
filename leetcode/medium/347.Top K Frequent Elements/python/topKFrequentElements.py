"""Top K Frequent Elements"""

def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        nums_frequency = {}
        for num in nums:
            if num not in nums_frequency:
                nums_frequency[num] = 1
            else:
                nums_frequency[num] += 1
        nums_frequency = sorted(nums_frequency.items(), key=lambda item: item[1], reverse=True)
        most_frequent_nums = [item[0] for item in nums_frequency[:k]]
        return most_frequent_nums

'''Complexity Analysis:
Time Complexity: O(N log N)
Space Complexity: O(N)'''