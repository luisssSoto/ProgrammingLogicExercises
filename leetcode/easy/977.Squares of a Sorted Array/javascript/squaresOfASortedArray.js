"use strict";

/**
 * @param {number[]} nums
 * @return {number[]}
 */

let sortedSquares = function(nums) {
    let squareNums = nums.map(number => {
        return number ** 2;
    });
    let isSorted = false;
    while (isSorted === false) {
        isSorted = true;
        for (let i = 0; i < squareNums.length - 1; i++) {
            if (squareNums[i] > squareNums[i + 1]) {
                isSorted = false;
                let tempNum = squareNums[i + 1];
                squareNums[i + 1] = squareNums[i];
                squareNums[i] = tempNum;
            };
        };
    };
    return squareNums;
};

//for iterate nums
//square each number
//sort burble method all array

let testData = [-4,-1,0,3,10];
let testData1 = [-7,-3,2,3,11];
console.log(sortedSquares(testData));

// Approach 2: Two Pointer Technique
var sortedSquares1 = function(nums) {
    let insertPointer = nums.length - 1; 
    let rightPointer = nums.length - 1;
    let leftPointer = 0;
    let sortedSquareArray = nums.slice()
    for (let i = insertPointer; i >= 0; i--) {
        let square;
        if (Math.abs(nums[leftPointer]) < Math.abs(nums[rightPointer])) {
            square = nums[rightPointer] ** 2;
            rightPointer -= 1;
        } else {
            square = nums[leftPointer] ** 2;
            leftPointer += 1;
        };
        sortedSquareArray[i] = square;
    };
    return sortedSquareArray;
};

console.log(sortedSquares1(testData));
/**
 * Complexity Analysis:
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(N) if you take output into account and O(1) otherwise.
 */