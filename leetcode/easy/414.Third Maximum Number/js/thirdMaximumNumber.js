"use strict";

/**
 * @param {number[]} nums
 * @return {number} third distinct maximum number 
 * @author AlexSoto
 */

// 1. sort array burble method descending order
// 2. maxNumber = -999_999_999, countMaxNumber = 0
// 3. while countMaxNumber === 3...
// 3.1 for i equal 0, while i < nums length...
// 3.1.1 if i equal 0 and nums[i] > maxNumber....
// 3.1.1.1 countMaxNumber += 1
// 3.1.1.2 maxNumber = nums[i]
// 3.1.1 else if nums[i] < maxNumber...
// 3.1.1.1 countMaxNumber += 1
// 3.1.1.2 maxNumber = nums[i]
// 3.1.1 else countMaxNumber === 3:
// 3.1.1.1 return maxNumber
// 4. return maxNumber

var thirdMax = function(nums) {
    console.log(nums);
    let isItSorted = false;
    while (isItSorted === false) {
        isItSorted = true;
        for (let i = 0; i < nums.length - 1; i++) {
            if (nums[i] < nums[i + 1]) {
                let temp = nums[i];
                nums[i] = nums[i + 1];
                nums[i + 1] = temp;
                isItSorted = false;
            };
        };
    };
    console.log(nums);
    let maxNumber = nums[0];
    let countMaxNumber = 1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] < maxNumber) {
            maxNumber = nums[i];
            countMaxNumber++;
        };
        if (countMaxNumber === 3) {
            return maxNumber;
        };
    };
    if (countMaxNumber != 3) {
        return nums[0];
    };
};

// Testing
let nums0 = [3,2,1];
let nums1 = [1,2];
let nums2 = [2,2,3,1];
let nums3 = [1,2,2,5,3,5];
console.log(thirdMax(nums3));