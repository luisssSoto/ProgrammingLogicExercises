# When I didn't know the linked lists:
def middle_node(head):
    return head[len(head) // 2:]

#1. input: array integers
#   output: integers array

#2. knowing the middle element

#3. divide the half of the length of the array
#   create another list since the half of the array to the end
#   return the array

#4. any problem just coding!

test1 = [1,2,3,4,5]
print(middle_node(test1))


# Current Approach
class ListNode:
     def __init__(self, val):
          self.val = val
          self.next = None

def middle_node(head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print(f"middle val: {slow.val}")
        return slow

ln1 = ListNode(1)
ln2 = ListNode(2)
ln3 = ListNode(3)
ln4 = ListNode(4)
ln5 = ListNode(5)
ln6 = ListNode(6)

ln1.next = ln2
ln2.next = ln3
ln3.next = ln4
ln4.next = ln5

print(middle_node(ln1))

ln5.next = ln6

print(middle_node(ln1))