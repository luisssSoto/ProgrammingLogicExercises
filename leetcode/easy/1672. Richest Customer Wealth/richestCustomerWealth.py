"""Richest Customer Wealth"""
def maximumWealth(accounts):
    richest_money = 0
    for account in accounts:
        total = 0
        for amount in account:
            total += amount
        richest_money = max(richest_money, total)
    return richest_money

#1. input: array
#   output: integer the greater value of the list inside the array

#2. two for loops
#   a variable to sum each list inside the array
#   create another empty list to save the addition's accounts
#   for loop to discover the maximum value
#   return the maximum value

#3. create an empty list
#   iterate through the array then
#   create a variable to add all the values of each account
#   iterate for all the values inside the list
#   start to add all the values to the addition variable
#   once the addition is complete append it to the empty list
#   once the last iteration done
#   create a variable max_num and assign it the first element of the empty list
#   iterate the empty list since the second value to the end
#   if the value is greater than the max_num, replace it 
#   once the iteration is done, return the max_num

#4. all looks great.... Coding!

test1 = [[1,2,3],[3,2,1]]
print(maximumWealth(test1))

test2 = [2,9,3,6]
print(max(test2))