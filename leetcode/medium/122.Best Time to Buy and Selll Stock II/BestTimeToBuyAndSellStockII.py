"""Best Time to Buy and Sell Stock II"""
def max_profit(prices):
    pass

'''
1. 
input: integer array
output: integer number with the most profit

2.
iterate prices
while condition and prove all the posibilities
for loop i in range
    conditional statement if the arr[i] < arr[i + 1] then
        profit += arr[i + 1] - arr[i]
        del arr[i]
        del arr[i + 1]
    new_array.append(profit)
        
'''