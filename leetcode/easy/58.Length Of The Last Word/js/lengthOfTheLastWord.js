"use strict";

// Length of the Last Word

/**
 * 
 * @param {string} s
 * @return {number} 
 */
var lengthLastWord = function(s) {
    s = s.trim();
    let count = 0;
    let pointer = s.length - 1;
    while (pointer !== -1 && s[pointer] !== " ") {
        count++;
        pointer--;
    };
    return count;
};

// Testing
let s0 = "Hello World";
console.log(lengthLastWord(s0));

// Complexity Analysis:
// Time Complexity: O(N)
// Space Complexity: O(1)
