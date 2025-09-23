"""Best Time to Buy and Sell Stock"""

def maxProfit(prices):
    min_price = float("inf")
    greater_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > greater_profit:
            greater_profit = prices[i] - min_price
    return greater_profit

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''