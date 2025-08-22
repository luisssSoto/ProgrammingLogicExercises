"Electronics Shop"
def get_money_spent(keyboards, drives, b):
    money_spent = -1
    options = []
    for keyboard in keyboards:
        for drive in drives:
            money_spent = keyboard + drive
            if money_spent == b:
                return money_spent
            elif money_spent < b:
                options.append(money_spent)
    if len(options) >= 1:
        return max(options)
    else:
        return -1
    
'''Complexity Analysis:
Time Complexity: O(N * M)
Space Complexity: O(N)'''