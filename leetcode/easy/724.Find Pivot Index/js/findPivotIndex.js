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
let dataTesst0 = [1,7,3,6,5,6];
let dataTesst1 = [1,2,3];
let dataTesst2 = [2,1,-1];
let dataTesst3 = [-1,-1,0,1,1,0];
let dataTesst4 = [4];

console.log(findPivotIndex(dataTesst4));