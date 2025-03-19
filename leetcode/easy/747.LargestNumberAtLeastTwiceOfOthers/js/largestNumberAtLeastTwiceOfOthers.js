"use strict";
/**
 * @param {number[]} nums
 * @return {number} 
 */

var dominantIndex = function(nums) {
    let greaterValue = -999_999_999;
    let greaterValueIndex = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > greaterValue){
            greaterValueIndex = i;
            greaterValue = nums[i];
        };
    };
    for (let i = 0; i < nums.length; i++){ 
        for (let j = 0; j < nums.length - i - 1; j++){
            if (nums[j] > nums[j + 1]) {
                let temp = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = temp;
            };
        };
    };
    let secondGreaterValue = nums[nums.length - 2];
    if (secondGreaterValue * 2 <= greaterValue) {
        return greaterValueIndex;
    } else {
        return -1;
    };
};

// Testing
let nums = [3,2,1,6];
let nums1 = [1,2,3,4];
let nums2 = [0,0,0,1];
console.log(dominantIndex(nums1));
