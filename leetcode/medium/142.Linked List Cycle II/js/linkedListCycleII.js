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
    let tortoise = head;
    let hare = head;
    while (hare !== null && hare.next !== null) {
        tortoise = tortoise.next;
        hare = hare.next.next;
        if (tortoise === hare) {
            hare = head;
            while (hare !== tortoise) {
                hare = hare.next;
                tortoise = tortoise.next;
            };
            return tortoise;
        };
    };
    return null;
};
// Complexity Analysis:
// Time Complexity: O(N)
// Space Complexity: O(1)