"use strict";
/**
 * @param {number[]} nums
 * @return {number}
 * @author AlexSoto
 */
var findMaxConsecutiveOnes = function (nums) {
    let countOnes = 0;
    let greatestSequence = 0;
    for (let i = 0; i < nums.length; i ++) {
        if (nums[i] === 1) {
            countOnes += 1;
        } else {
            greatestSequence = Math.max(greatestSequence, countOnes);
            countOnes = 0;
        }        
    }
    return Math.max(greatestSequence, countOnes)
}; 

//Testing 
let n = [1, 1, 0, 1, 1, 1]
console.log(findMaxConsecutiveOnes(n));

/**
 * Complexity Analysis:
 * Time complexity = O(N) Where N is the number of elements in the array
 * Space complexity = O(1) We do not use any extra space
 */