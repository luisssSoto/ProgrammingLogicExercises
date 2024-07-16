"""Remove Duplicates From Sorted Array"""
def remove_duplicates(nums):
    count = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
                del nums[j]
                nums.insert(0, 'z')
    for k in range(count):
        del nums[0]
    return len(nums)

test1 = [0,0,0,0,0]
print(remove_duplicates(test1))


#1. input: integer array
#   output: integer value: the length of unique values inside the modified array previously pass

#2. iterate nums
#   two for loop maybe
#   conditional statement if the element is more once delete all the copies
#   return the lengt of the array

#3. iterate nums with range(len(nums))
#   iterate nums again and compare each nums[i] element with nums[j] element
#   if nums[i] == nums[j] then...
#   del nums[j]
#   nums.insert(0, 0)
#   count +=1
#   iterate again to delete the first values according count variable
#   return the length of the array

#4. coding but be careful with delete instruction