"use strict";

// Design Linked List

/**
 * @param {number} index
 * @return {number}
 */

class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    };
};

var MyLinkedList = function() {
    this.size = 0;
    this.head = new Node(0);    
};

/**
 * 
 * @param {number} index
 * @return {number} 
 */
MyLinkedList.prototype.get = function(index) {
    if (index < 0 || index >= this.size) {
        return -1;
    };
    let current = this.head;
    for (let i = 0; i < index + 1; i++) {
        current = current.next;
    };
    return current.val;
};

/**
 * 
 * @param {number} val
 * @return {void} 
 */
MyLinkedList.prototype.addAtHead = function(val) {
    this.addAtIndex(0, val);
}

/**
 * 
 * @param {number} val
 * @return {void} 
 */
MyLinkedList.prototype.addAtTail = function(val) {
    this.addAtIndex(this.size, val);
}

/**
 * 
 * @param {number} index 
 * @param {number} val 
 * @return {void}
 */
MyLinkedList.prototype.addAtIndex = function(index, val) {
    if (index > this.size) {
        return;
    };
    if (index < 0) {
        index = 0;
    };
    this.size++;
    let predecessor = this.head;
    for (let i = 0; i < index; i++) {
        predecessor = predecessor.next;
    };
    let toAdd = new Node(val);
    toAdd.next = predecessor.next;
    predecessor.next = toAdd;
};

/**
 * 
 * @param {number} index
 * @return {void} 
 */
MyLinkedList.prototype.deleteAtIndex = function(index) {
    if (index < 0 || index >= this.size) {
        return;
    };
    this.size--;
    let predecessor = this.head;
    for (let i = 0; i < index; i++) {
        predecessor = predecessor.next;
    };
    predecessor.next = predecessor.next.next;
};

// Testing
let dt0 = ["MyLinkedList","addAtHead","addAtTail","addAtTail","addAtTail","addAtTail","addAtTail","addAtTail","deleteAtIndex","addAtHead","addAtHead","get","addAtTail","addAtHead","get","addAtTail","addAtIndex","addAtTail","addAtHead","addAtHead","addAtHead","get","addAtIndex","addAtHead","get","addAtHead","deleteAtIndex","addAtHead","addAtTail","addAtTail","addAtIndex","addAtTail","addAtHead","get","addAtTail","deleteAtIndex","addAtIndex","deleteAtIndex","addAtHead","addAtTail","addAtHead","addAtHead","addAtTail","addAtTail","get","get","addAtHead","addAtTail","addAtTail","addAtTail","addAtIndex","get","addAtHead","addAtIndex","addAtHead","addAtTail","addAtTail","addAtIndex","deleteAtIndex","addAtIndex","addAtHead","addAtHead","deleteAtIndex","addAtTail","deleteAtIndex","addAtIndex","addAtTail","addAtHead","get","addAtIndex","addAtTail","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","deleteAtIndex","get","get","addAtHead","get","addAtTail","addAtTail","addAtIndex","addAtIndex","addAtHead","addAtTail","addAtTail","get","addAtIndex","addAtHead","deleteAtIndex","addAtTail","get","addAtHead","get","addAtHead","deleteAtIndex","get","addAtTail","addAtTail"]
let dt1 = [[],[38],[66],[61],[76],[26],[37],[8],[5],[4],[45],[4],[85],[37],[5],[93],[10,23],[21],[52],[15],[47],[12],[6,24],[64],[4],[31],[6],[40],[17],[15],[19,2],[11],[86],[17],[55],[15],[14,95],[22],[66],[95],[8],[47],[23],[39],[30],[27],[0],[99],[45],[4],[9,11],[6],[81],[18,32],[20],[13],[42],[37,91],[36],[10,37],[96],[57],[20],[89],[18],[41,5],[23],[75],[7],[25,51],[48],[46],[29],[85],[82],[6],[38],[14],[1],[12],[42],[42],[83],[13],[14,20],[17,34],[36],[58],[2],[38],[33,59],[37],[15],[64],[56],[0],[40],[92],[63],[35],[62],[32]]

let obj = new MyLinkedList();
obj.addAtHead(38);
obj.addAtTail(66);
obj.addAtTail(61);
obj.addAtTail(76);
obj.addAtTail(26);
obj.addAtTail(37);
obj.addAtTail(8);
obj.deleteAtIndex(5);
obj.addAtHead(4);
obj.addAtHead(45);
console.log(obj.get(4));

// Complexity Analysis
// Time complexity: O(1) for addAtHead. O(k) for get, addAtIndex, 
// and deleteAtIndex, where k is an index of the element to get, add 
// or delete. O(N) for addAtTail.
// Space complexity: O(1) for all operations.