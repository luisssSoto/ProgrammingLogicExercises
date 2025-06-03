"use strict";

// Linked List Cycle

/**
 * 
 * @param {ListNode} head 
 */
// Approach 1: HashTable
var linkedListCycle = function(head) {
    let mySet = new Set();
    while (head !== null) {
        if (mySet.has(head)) {
            return true;
        };
        mySet.add(head);
        head = head.next;
    };
    return false;
};

// Complexity Analysis:
// Time Complexity: O(N)
// Space Complexity: O(N)

// Approach 2: Floyd's Cycle Finding Algorithm

/**
 * 
 * @param {ListNode} head 
 */
var hasCycle = function(head) {
    if (head === null) {
        return false;
    };
    let slow = head;
    let fast = head.next;
    while (slow !== fast) {
        if (fast === null || fast.next === null) {
            return false;
        };
        slow = slow.next;
        fast = fast.next.next;
    };
    return true;
};
// Complexity Analysis:
// Time Complexity: O(N)
// Space Complexity: O(1)