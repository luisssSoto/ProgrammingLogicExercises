"use strict";
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number} it will return the length of the array
 */

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
