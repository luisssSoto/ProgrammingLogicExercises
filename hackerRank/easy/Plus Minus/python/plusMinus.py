"""Plus Minus"""

def plus_minus(arr):
    nums_dict = {"positive": 0, "negative": 0, "zeroes": 0}
    for num in arr:
        if num > 0:
            nums_dict["positive"] += 1
        elif num < 0:
            nums_dict["negative"] += 1
        else: 
            nums_dict["zeroes"] +=1
    print(round(nums_dict["positive"]/len(arr), 6))
    print(round(nums_dict["negative"]/len(arr), 6))
    print(round(nums_dict["zeroes"]/len(arr), 6))


# Testing
a = [-4,3,-9,0,4,1]
plus_minus(a)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity O(1)'''