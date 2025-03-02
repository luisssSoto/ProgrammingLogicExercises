"use strict";
/**
 * @param {number[]} arr
 * @return {boolean} if the arr is a mountain array
 */

// 1. edge cases arr length >= 3
// 2. var isItDecreasing = false, isItAscending = false
// 3. for from i + 1 until arr length;
// 3.1. if arr[i] > arr[i - 1]... isItAscending = true
// 3.2. else if arr[i] < arr[i - 1]... isItDescending = true
// 3.3. if isItDescending === true && arr[i] >= arr[i - 1]... return false
// 4. if isItAscending === false... return false
// 5. return true

var validMountainArray = function(arr) {
    if (arr.length < 3) {
        return false;
    } else {
        let isItDecreasing = false;
        let isItAscending = false;
        for (let i = 1; i < arr.length; i++) {
            if (arr[i] > arr[i - 1]) {
                isItAscending = true;
            } else if (arr[i] < arr[i -1]) {
                isItDecreasing = true;
            } else if(arr[i] === arr[i - 1]) {
                return false;
            }
            if (arr[i] > arr[i - 1] && isItDecreasing === true) {
                return false;
            };
        };
        if (isItDecreasing === false || isItAscending === false) {
            return false;
        };
        return true;
    };
};

// Testing
let nums1 = [2,1];
let nums2 = [3,5,5];
let nums3 = [0,3,2,1];
console.log(validMountainArray(nums3))