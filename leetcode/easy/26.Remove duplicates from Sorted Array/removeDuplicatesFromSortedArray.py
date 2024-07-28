"""Remove Duplicates From Sorted Array"""
def remove_duplicates(nums):
    count = 0
    duplicates_index = []
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            duplicates_index.append(i)
    for index in duplicates_index:
        del nums[index - count]
        count += 1
    return len(nums)
            
test0 = [0,0,1,1,1,2,2,3,3,4]
test1 = [1,1,2]
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

# Above approach wasn't work, 😕 but I found another one ☺️

'''smarter approach and reducess time complexity'''
def removeDuplicates(nums):
        nums[:]=list(sorted(set(nums)))
        print(nums)
        return len(nums)

test0 = [1,1,2]
print(removeDuplicates(test0))
