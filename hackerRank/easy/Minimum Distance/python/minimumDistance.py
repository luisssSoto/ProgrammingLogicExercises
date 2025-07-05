def minimum_distances(a):
    # Write your code here
    min_dis = 999_999_999
    right = len(a) - 1
    for left in range(len(a) - 1):
        while right > left:    
            if a[left] == a[right]:
                curr = right - left
                min_dis = min(min_dis, curr)
                right = len(a) - 1
                break
            else:
                right -= 1
            if right == left:
                right = len(a) - 1
                break
    if min_dis == 999_999_999:
        return - 1
    else:
        return min_dis
    
# Testing
data_a = [3,2,1,2,3]
data_b = [1,1]
print(minimum_distances(data_b))

'''Complexity Analysis:
Time Complexity: O(N2)
Space Complexity: O(1)'''
    