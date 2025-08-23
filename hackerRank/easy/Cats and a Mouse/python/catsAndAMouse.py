"""Cats and a Mouse"""

def cat_and_mouse(x, y, z):
    distance_cat_a = abs(x - z)
    distance_cat_b = abs(y - z)
    if distance_cat_a == distance_cat_b:
        return "Mouse C"
    elif distance_cat_a > distance_cat_b:
        return "Cat B"
    else:
        return "Cat A"
    
'''Complexity Analysis:
Time Complexity: O(1)
Space Complexity: O(1)'''