"""Third Maximum Number"""
def third_maximum_number(nums):
    if len(nums) <= 2:
        return max(nums)
    else:
        set_nums = set(nums)
        print(set_nums)

l = [x for x in range(3, 0, -1)]
l.append(0)
print(third_maximum_number(l))

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