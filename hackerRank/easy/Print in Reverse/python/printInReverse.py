"""Print in Reverse"""
def reversePrint(llist):
    nodes_data = []
    while llist is not None:
        nodes_data.append(llist.data)
        llist = llist.next
    for i in range(len(nodes_data) - 1, -1, -1):
        print(nodes_data[i])

def reverse_print(llist):
    prev = None
    curr = llist
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    while prev is not None:
        print(prev.data)
        prev = prev.next