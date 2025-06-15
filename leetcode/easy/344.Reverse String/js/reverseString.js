"use strict";

// Approach 1: Two Pointers Technique
/**
 * 
 * @param {character[]} s
 * @returns {void} Do not return anything, modify s in-place instead. 
 */
var reverseString = function(s) {
    let startPointer = 0;
    let endPointer = s.length - 1;
    for (let i = 0; i < Math.round(s.length / 2); i++) {
        let temp = s[startPointer];
        s[startPointer] = s[endPointer];
        s[endPointer] = temp;
        startPointer++;
        endPointer--;
    };
    return s;
};

// Testing 
let s0 = ["h","e","l","l","o"];
let s1 = ["H","a","n","n","a","h"];
console.log(reverseString(s1));

// Complexity Analysis:
// Time Complexity: O(N)
// Space Complexity: O(1)

// Approach 2: Recursion and Two Pointers Technique
var reverseString = function(s) {
    var helper = function(s, startPointer, endPointer) {
        if (startPointer === Math.floor(s.length / 2)) {
            return s;
        } else {
            let temp = s[startPointer];
            s[startPointer] = s[endPointer];
            s[endPointer] = temp;
            return helper(s, ++startPointer, --endPointer);
        };
    };
    let startPointer = 0;
    let endPointer = s.length - 1;
    return helper(s, startPointer, endPointer);
};

// Testing 
let s00 = ["h","e","l","l","o"];
let s01 = ["H","a","n","n","a","h"];
console.log(reverseString(s00));
console.log(reverseString(s01));