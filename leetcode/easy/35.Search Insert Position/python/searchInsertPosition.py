"""Search Insert Position"""

def search_insert_position(nums, target):
    def helper(arr, tar):
        left_pointer = 0
        right_pointer = len(arr) - 1
        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2
            if arr[middle_pointer] == tar:
                return middle_pointer
            elif arr[middle_pointer] > tar:
                right_pointer = middle_pointer
                right_pointer -= 1
            elif arr[middle_pointer] < tar:
                left_pointer = middle_pointer
                left_pointer += 1
        return middle_pointer
    index = helper(nums, target)
    if target < nums[index] or target == nums[index]:
        return index
    else:
        return index + 1

#Testing
nums0 = [1,3,5,6]
target0 = 7
nums1 = [1,3]
target1 = 0
print(search_insert_position(nums0, target0))

'''Complexity Analysis
Time complexity : O(logN).
Space complexity: O(1)'''