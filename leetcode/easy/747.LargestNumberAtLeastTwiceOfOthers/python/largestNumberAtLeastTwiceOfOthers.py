def dominant_index(nums):
    greater_num = -999
    previous_greater_num = 0
    greater_num_index = -1
    for i in range(len(nums)):
        if nums[i] > greater_num:
            previous_greater_num = greater_num
            greater_num = nums[i]
            greater_num_index = i
        if nums[i] > previous_greater_num and nums[i] < greater_num: 
            previous_greater_num = nums[i]
    if previous_greater_num * 2 <= greater_num:
        return greater_num_index
    else:
        return -1

# Testing
nums = [3,2,1,6]
nums1 = [1,2,3,4]
nums2 = [0,0,0,1]
nums3 = [0,0,3,2]
print(dominant_index(nums3))