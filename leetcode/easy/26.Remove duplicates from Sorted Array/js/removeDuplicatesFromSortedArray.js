"use strict";
/**
 * @param {number[]} nums
 * @return {number}
 */

var removeDuplicates = function(nums) {
    console.log(nums);
    let assignationPointer = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== nums[i - 1]) {
            nums[assignationPointer] = nums[i];
            assignationPointer++;
        };
    };
    console.log(nums);
    return assignationPointer;
};

let nums = [0,0,1,1,1,2,2,3,3,4];
let nums1 = [1,1,2]
console.log(removeDuplicates(nums));