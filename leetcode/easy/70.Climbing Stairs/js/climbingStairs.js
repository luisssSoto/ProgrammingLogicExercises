"use strict";

// Approach 4: Fibonacci Number

/**
 * 
 * @param {number} n
 * @return {number} 
 */
var climbingStairs = function(n) {
    if (n === 1) {
        return 1;
    };
    let first = 1;
    let second = 2;
    for (let i = 3; i < n + 1; i++) {
        let third = first + second;
        first = second;
        second = third;
    };
    return second;
};

// Complexity Analysis:
// Time Complexity: O(N)
// Space Complexity: O(1)