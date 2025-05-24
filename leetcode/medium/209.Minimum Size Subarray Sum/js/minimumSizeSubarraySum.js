"use strict";
// Minimum Size Subarray Sum

var minimumSize = function(target, nums) {
    let leftPointer = 0;
    let sumOfCurrentWindow = 0;
    let result = Infinity;
    for (let rightPointer = 0; rightPointer < nums.length; rightPointer++) {
        sumOfCurrentWindow += nums[rightPointer];
        while (sumOfCurrentWindow >= target) {
            result = Math.min(result, rightPointer - leftPointer + 1);
            sumOfCurrentWindow -= nums[leftPointer];
            leftPointer++;
        };
    };
    if (result !== Infinity) {
        return result;
    } else {
        return 0;
    };
};

// Testing
let t = 7;
let n = [2,3,1,2,4,3];
console.log(minimumSize(t, n));