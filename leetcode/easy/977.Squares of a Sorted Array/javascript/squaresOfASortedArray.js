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