"use strict";
/**
 * @param {number[]} arr
 * @return {void} anything just modify the array (arr) in-place
 */

// 1. writePointer = 0
// 2. for readPointer = 0, readPointer < arr length
// 2.1 if arr[readPointer] not equal 0... 
// let temp = arr[writePointer] arr[writePointer] = arr[readPointer] arr[readPointer] = temp  
// writePointer += 1

var moveZeroes = function(arr) {
    let writePointer = 0;
    for (let readPointer = 0; readPointer < arr.length; readPointer++) {
        if (arr[readPointer] !== 0) {
            let temp = arr[writePointer];
            arr[writePointer] = arr[readPointer];
            arr[readPointer] = temp;
            writePointer++;
        };
    };
    return arr;
};
let nums = [0,1,0,3,12];
let nums1 = [0]
console.log(moveZeroes(nums1));
