"use strict";
// Two Sum II
/**
 * @param {Array int} numbers
 * @param {int} target
 * @return {Array int}
 * @author {Alex Soto}
 */

// Approach 1: Two Pointers
var twoSumII = function(numbers, target) {
    let leftPointer = 0;
    let rightPointer = numbers.length - 1;
    while (leftPointer < rightPointer) {
        let result = numbers[leftPointer] + numbers[rightPointer];
        if (result === target) {
            let sumIndexes = [];
            sumIndexes.push(leftPointer + 1);
            sumIndexes.push(rightPointer + 1);
            return sumIndexes;
        } else if (result > target) {
            rightPointer--;
        } else {
            leftPointer++;
        };
    };
    return [-1, -1]
};

// Testing
let n0 = [2,7,11,15]
let t0 = 9
let n1 = [2,3,4]
let t1 = 6
let n2 = [-1, 0]
let t2 = -1
let n3 = [5,25,75]
let t3 = 100
let n4 = [3,24,50,79,88,150,345]
let t4 = 200
let n5 = [];
for (let i = 0; i <= 197; i++) {
    n5.push(-1);
};
n5.push(1);
n5.push(1);
// console.log(n5);
let t5 = 2;
console.log(twoSumII(n5, t5));

// Complexity Analysis:
// Time Complexity: O(N)
// Space Complecity: O(1)