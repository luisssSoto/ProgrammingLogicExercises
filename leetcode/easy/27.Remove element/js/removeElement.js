"use strict";
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number} it will return the length of the array
 */

// In this solution you maintain all the elements
var removeElement = function (nums, val) {
    console.log(nums);
    let index = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== val) {
            let temp = nums[index];
            nums[index] = nums[i];
            nums[i] = temp
            index++
        };
    };
    console.log(nums);
    return index;
};

let nums = [0,1,2,2,3,0,4,2];
let val = 2;
let nums1 = [2, 2, 2, 1];
let val1 = 2;
let nums2 = [3,2,2,3];
let val2 = 3
console.log(removeElement(nums, val));

// Approach 1: Two Pointers Techique while
var removeElement1 = function(nums, val) {
    let writerPointer = 0;
    let readerPointer = 0;
    while (readerPointer < nums.length) {
        if (nums[readerPointer] !== val) {
            nums[writerPointer++] = nums[readerPointer++];
        } else {
            readerPointer++;
        };
    };
    console.log(nums);
    return writerPointer;
};

// Approach 1: Two Pointers Technique for
var removeElement2 = function(nums, val) {
    let writerPointer = 0;
    for (let readerPointer = 0; readerPointer < nums.length; readerPointer++) {
        if (nums[readerPointer] !== val) {
            nums[writerPointer++] = nums[readerPointer];
        };
    };
    console.log(nums);
    return writerPointer;
};

//Testing 
let nums10 = [0,1,2,2,3,0,4,2];
console.log(removeElement2(nums10, 2))

/**
 * Complexity analysis

Time complexity : O(n).
Assume the array has a total of n elements, both i and j traverse at most 2n steps.

Space complexity : O(1).
 */