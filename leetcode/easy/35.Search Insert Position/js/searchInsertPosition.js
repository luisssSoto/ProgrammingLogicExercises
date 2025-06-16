"use strict";
// Search Insert Position

/**
 * 
 * @param {number[]} nums 
 * @param {number} target
 * @returns {number} 
 */

var searchInsertPosition = function(nums, target) {
    let leftPointer = 0;
    let rightPointer = nums.length - 1;
    let middlePointer = 0;
    while (leftPointer <= rightPointer) {
        middlePointer = Math.floor((leftPointer + rightPointer) / 2);
        if (nums[middlePointer] === target) {
            return middlePointer;
        } else if (nums[middlePointer] > target) {
            rightPointer = middlePointer;
            rightPointer--;
        } else if (nums[middlePointer] < target) {
            leftPointer = middlePointer;
            leftPointer++;
        };
    };
    if (target < nums[middlePointer] || target === nums[middlePointer]) {
        return middlePointer;
    } else {
        return middlePointer + 1;
    };
};

//Testing
let nums0 = [1,3,5,6];
let target0 = 10;
let nums1 = [1,3];
let target1 = 3;
console.log(searchInsertPosition(nums1, target1));

// Complexity Analysis
// Time complexity : O(logN).
// Space complexity: O(1)