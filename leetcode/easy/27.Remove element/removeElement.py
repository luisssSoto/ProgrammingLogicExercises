"""Remove Element"""

def removeElement(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] == val:
            nums.append(nums[i])
            del nums[i]
            nums.insert(0, 0)
            count += 1
    for j in range(count):
        del nums[0]
        del nums[-1]
    return len(nums)

n = [0,1,2,2,3,0,4,2]
v = 2
print(removeElement(n, v))

#1. input: nums list, integer value
#   output: nums list with all the elements except the integer value and also its length

#2. iterate the list
#   conditional statement: if nums[i] == val
#   if so... delete it
#   returns the length of the list and the modified list

#3. iterate the list
#   conditional statemtent: if nums[i] == val
#   if so.. del nums[i]
#   return len(nums) and nums

#4. coding