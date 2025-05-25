"use strict";
// Rotate Array 

/**
 * @param {Array int} nums
 * @param {int} k
 * @return {Array int} nums
 */

var rotateArray = function(nums, k) {
    let spacesToMove = k % nums.length;
    if (spacesToMove === 0) {
        return nums;
    };
    let beginNums = nums.slice(nums.length - spacesToMove);
    let writePointer = nums.length - 1;
    for (let i = nums.length - spacesToMove - 1; i >= 0; i--) {
        nums[writePointer] = nums[i];
        writePointer--;
    };
    for (let i = 0; i < beginNums.length; i++) {
        nums[i] = beginNums[i];
    };
    return nums;
};

// Testing 
let nums0 = [1,2,3,4,5,6,7]
let k0 = 3
console.log(rotateArray(nums0, k0))