var swapPairs = function (head) {
    let dummy = new ListNode(-1);
    dummy.next = head;
    let prevNode = dummy;
    while (head !== null && head.next !== null) {
        let firstNode = head;
        let secondNode = head.next;
        prevNode.next = secondNode;
        firstNode.next = secondNode.next;
        secondNode.next = firstNode;
        prevNode = firstNode;
        head = firstNode.next;
    }
    return dummy.next;
};

// Complexity Analysis:
// Time Complexity : O(N) where N is the size of the linked list.
// Space Complexity : O(1).