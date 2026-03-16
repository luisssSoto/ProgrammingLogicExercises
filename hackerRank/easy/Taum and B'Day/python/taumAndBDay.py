def taumBday(b, w, bc, wc, z):
    a_price = (b * bc) + (w * wc)
    b_price = (b + w) * bc + (z * w)
    c_price = (b + w) * wc + (z * b)
    return min(a_price, b_price, c_price)

'''Complexity Analysis:
Time Complexity: O(1)
Space Complexity: O(1)'''