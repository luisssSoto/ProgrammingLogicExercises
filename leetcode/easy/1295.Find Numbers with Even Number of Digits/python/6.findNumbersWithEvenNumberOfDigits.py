"""Find Numbers With Even Number of Digits"""
# Approaching 2: Cast in String
def find_numbers(nums):
    even_counter = 0
    for i in range(len(nums)):
        if len(str(nums[i])) % 2 == 0: even_counter += 1
    return even_counter

test1 = [12,345,2,6,7896]
test2 = [555,901,482,1771]
print(find_numbers(test2))

'''Complexity Analysis:
Time complexity: O(N . log(M))
Where M is each num in nums because we cast each num into String
Then we perform a loop of each num: O(N)
Where N is nums
Space complexity: We are using constant extra space. Hence, the space complexity is O(1).
 '''

# Approaching 1: Extract digits
def find_numbers1(nums):
    def has_even_digits(num):
        count_digits = 0
        while num != 0:
            count_digits += 1
            num //= 10
        # or count_digits % 2 == 0
        return (count_digits & 1) == 0
    even_digit_count = 0
    for num in nums:
        if has_even_digits(num):
            even_digit_count += 1
    return even_digit_count

print(find_numbers1(test1))
print(find_numbers1(test2))

'''Complexity Analysis:
Time complexity: O(N . log(M))
When dividing an integer x by y, there can be at most O(log y(x)) divisions: O(log M)
Where M is each num in nums
Then we perform a loop of each num: O(N)
Where N is nums
Space complexity: We are using constant extra space. Hence, the space complexity is O(1).
 '''

# Approaching 4: Constraint Analysis
#1≤nums[i]≤10 pow 5
def find_numbers2(nums):
    even_digit_count = 0
    for num in nums:
        if (num >= 10 and num <= 99) or (num >= 1000 and num <= 9999) or (num == 100_000):
            even_digit_count += 1
    return even_digit_count

'''Complexity Analysis:
Time complexity: O(N)
Space complexity: O(1)'''
