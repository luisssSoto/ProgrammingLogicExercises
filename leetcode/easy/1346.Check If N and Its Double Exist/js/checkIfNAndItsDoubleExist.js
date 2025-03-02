"use strict";
/**
 * @param {number[]} arr
 * @return {boolean}
 */

// 1. edge cases: length <= 1 return false
// 2. for length - 1 i = 0
// 3. vars divisionResult multiplicationResult
// 4. for arr length j = i
// 5. if arr[j + 1] === divisionResult or === multiplicationResult
// 6. return true
// 7.return false

var checkIfExist = function(arr) {
    if (arr.length <= 1) {
        return false;
    } else {
        for (let i = 0; i < arr.length - 1; i++) {
            let divisionResult = arr[i] / 2;
            let multiplicationResult = arr[i] * 2;
            for (let j = i; j < arr.length; j++) {
                if (arr[j + 1] === divisionResult || arr[j + 1] === multiplicationResult) {
                    return true;
                };
            };
        };
    };
    return false;
};
// Testing
let nums = [10,2,5,3];
let nums1 = [3,1,7,11];
let nums2 = [2,3,3,0,0]
console.log(checkIfExist(nums1));