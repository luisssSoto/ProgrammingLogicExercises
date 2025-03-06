"use strict";
 
/**
 * @param {number[]} nums
 * @return {number[]} modified nums
 * @author AlexSoto
 */

// 1. writePointer equal zero
// 2. for readPointer equal zero while readPointer < nums length...
// .. if nums[readPointer] % 2 equal 0 ...
// .. temp = nums[writePointer] nums[writePointer] = nums[readPointer] nums[readPointer] = temp
// .. writePointer += 1
// 3. return nums 

var sortArrayByParity = function(nums) {
    let writePointer = 0;
    for (let readPointer = 0; readPointer < nums.length; readPointer++) {
        if (nums[readPointer] % 2 === 0) {
            let temp = nums[writePointer];
            nums[writePointer] = nums[readPointer];
            nums[readPointer] = temp;
            writePointer++;
        };
    };
    return nums;
};

// Testing
let nums = [3,1,2,4];
let nums1 = [0];
console.log(sortArrayByParity(nums1));