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

// My Approach: Similar Brute Force but more efficient
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

/**Complexity Analysis:
 * Time complexity: O(n2)
 * Space complexity: O(1)
 */

// Approach 1: Brute Force
var checkIfExist = function(arr) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length; j++) {
            if ((arr[i] * 2 === arr[j] || arr[i] / 2 === arr[j]) && (i !== j)) {
                return true;
            };
        };
    };
    return false;
};

// Testing
let dataTest0 = [3,1,7,11];
console.log(checkIfExist(dataTest0));

/**
 * Complexity Analysis:
 * Time complexity: O(n2)
 * Space complexity: O(1)
 */

// Approach 2: Set and Lookup
var checkIfExist = function(arr) {
    let set1 = new Set();
    for (let num of arr) {
        if (set1.has(num * 2) || set1.has(num / 2)) {
            return true;
        };
        set1.add(num);
    };
    console.log(set1);
    return false;
};

// Testing
let dataTest1 = [10,2,5,3];
console.log(checkIfExist(dataTest1));

/** Complexity Analysis:
 * Time complexity: O(n)
 * Space complexity: O(n)
 */

// Approach 3: Sorting and Binary Search
var checkIfExist = function(arr) {
    arr.sort((a, b) => a - b);
    var binarySearch = function(target, array) {
        let begining_pointer = 0;
        let last_pointer = arr.length - 1;
        while (begining_pointer <= last_pointer) {
            let middle_pointer = Math.floor((begining_pointer + last_pointer) / 2);
            let guess = arr[middle_pointer];
            if (guess === target) {
                return middle_pointer;
            } else if (guess > target) {
                last_pointer = middle_pointer;
                last_pointer -= 1;
            } else if (guess < target) {
                begining_pointer = middle_pointer;
                begining_pointer += 1;
            };
        };
        return -1;
    };
    let index = -1;
    for (let i = 0; i < arr.length; i++) {
        index = binarySearch(arr[i] * 2, arr);   
        if (index >= 0 && i !== index) {
            return true;
        };
    };
    return false;
};

// Testing
let dataTest2 = [10,2,5,3];
let dataTest3 = [0, -2, 2];
console.log(checkIfExist(dataTest3));

/**Complexity Analysis:
Time complexity: O(nlogn)
Space complexity: O(n) or O(logn)
The space taken by the sorting algorithm depends on the language of implementation:
Space complexity: O(n) or O(logn) 
Sort and has a space complexity of O(n). */