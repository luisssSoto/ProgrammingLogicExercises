"""Third Maximum Number"""
def third_maximum_number(nums):
    set_nums = set(nums)
    if len(set_nums) <= 2:
        return max(nums)
    else:
        list_nums = list(set_nums)
        list_nums.sort() 
        list_nums = list_nums[-3:]
    return min(list_nums)
        

data1 = [-4,-5,-3,-2,-1]
print(third_maximum_number(data1))

'''
1.
input: integer array
output: integer number which is the result of figure out what is the distinct maximum number

2. 
edge cases: if lenght of nums <=2 return the maximum
key: sort the array
cast it to set
conditional statment to know if the set greater or equal to 3
return the min of that set

3. 
conditional statement if to know if nums <= 2 if so
    then return max(nums)
else:
    cast nums list to set
    sort set
    create a list from the last three elements
    return min(list)

4. happy coding!
'''