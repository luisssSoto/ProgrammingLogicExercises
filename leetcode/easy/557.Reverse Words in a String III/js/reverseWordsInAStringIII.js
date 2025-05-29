"use strict";

// Reverse Words in a String III

/**
 * @param {str} s
 * @return {str}
 */

var reverseWords = function(s) {
    let sArray = s.split("");
    console.log(`sArray: ${sArray}`);
    let rightPointer = 0;
    let leftPointer = 0;
    let lastSpaceIndex = 0;
    while (rightPointer < s.length) {
        if (sArray[rightPointer] === " " || rightPointer === s.length - 1) {
            lastSpaceIndex = rightPointer;
            if (rightPointer === s.length - 1) {
                rightPointer += 1;
            };
            let distance = Math.floor((rightPointer - leftPointer) / 2);
            for (let i = 0; i < distance; i ++) {
                let temp = sArray[leftPointer];
                sArray[leftPointer] = sArray[rightPointer - 1];
                sArray[rightPointer - 1] = temp;
                leftPointer++;
                rightPointer--;
            };
            rightPointer = lastSpaceIndex;
            leftPointer = rightPointer + 1;
        };
        rightPointer++;
    };
    return sArray.join("");
};

// Testing
let s = "Let's take LeetCode contest";
let s1 = "Hello World";
console.log(reverseWords(s1));