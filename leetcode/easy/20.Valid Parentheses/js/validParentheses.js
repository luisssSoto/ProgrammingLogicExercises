"use strict";

// Valid Parentheses

/**
 * 
 * @param {string} s 
 * @returns {boolean} 
 */
var validParentheses = function(s) {
    const mappings = {
        ")": "(",
        "}": "{",
        "]": "[",
    };
    const stack = [];
    for (let c of s) {
        if (mappings[c]) {
            const topElement = stack.length ? stack.pop() : "#";
            if (topElement !== mappings[c]) {
                return false;
            }
        } else {
            stack.push(c);
        }
    }
    return stack.length === 0;
};

// Complexity analysis
// Time complexity : O(n) because we simply traverse the given 
// string one character at a time and push and pop operations 
// on a stack take O(1) time.
// Space complexity : O(n) as we push all opening brackets onto 
// the stack and in the worst case, we will end up pushing all 
// the brackets onto the stack. e.g. ((((((((((.