"""Bill Division"""

def bon_appetit(bill, k, b):
    total = sum(bill)
    fair_bill = (total - bill[k]) // 2
    if fair_bill != b:
        print(b - fair_bill)
    else:
        print("Bon Appetit")

'''Complexity Analysis:
Time Complexity: O(N)
Space Compplexity: O(1)'''