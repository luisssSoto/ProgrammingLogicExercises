"""Print the Elements of a Linked List"""

def print_elements(head):
    while head is not None:
        print(head.data)
        head = head.next

'''Complexity Analysis: 
Time Complexity: O(N)
Space Complexity: O(1)'''