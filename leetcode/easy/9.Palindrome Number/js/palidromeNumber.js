"use strict";

// Palindrome Number
/**
 * @param {number} x
 * @return {boolean}
 */
//My Approach: Cast to String and then Two Pointers Techique
var isPalindrome = function(x) {
    x = String(x);
    let leftPointer = 0;
    let rightPointer = x.length - 1;
    while (leftPointer < rightPointer) {
        if (x[leftPointer] !== x[rightPointer]) {
            return false;
        };
        leftPointer++;
        rightPointer--;
    };
    return true;
};

// Complexity Analysis:
// Time Complexity: O(N)
// Space Complexity: O(1)