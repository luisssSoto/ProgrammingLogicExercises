"use strict";
//Find Pivot Index

/**
 * @param {array int} nums
 * @return {int} 
 * @author Alex Soto
 */ 

var findPivotIndex = function(nums) {
    nums.push(0);
    let leftSum = 0;
    let rightSum = 0;
    for (let i = 1; i < nums.length; i++) {
        rightSum += nums[i];
    };
    for (let i = 0; i < nums.length - 1; i++) {
        if (rightSum === leftSum) {
            return i;
        }
        else {
            leftSum += nums[i];
            rightSum -= nums[i + 1];
        };
    };
    return -1;
} ;

// Testing
let dataTest0 = [1,7,3,6,5,6];
let dataTest1 = [1,2,3];
let dataTest2 = [2,1,-1];
let dataTest3 = [-1,-1,0,1,1,0];
let dataTest4 = [4];

console.log(findPivotIndex(dataTest4));

// Complexity Analysis:
// Time Complexity: O(N2)
// Space Complexity: O(1)

// Approach 1: Prefix Sum
var findPivotIndex = function(nums) {
    let totalSum = nums.reduce((x, y) => x + y);
    let leftSum = 0;
    for (let i = 0; i < nums.length; i++) {
        if (leftSum === (totalSum - leftSum - nums[i])) {
            return i;
        };
        leftSum += nums[i];
    };
    return -1;
};

// Complexity Analysis:
// Time Complexity: O(N), where N is the length of nums.
// Space Complexity: O(1), the space used by leftSum and totalSum.