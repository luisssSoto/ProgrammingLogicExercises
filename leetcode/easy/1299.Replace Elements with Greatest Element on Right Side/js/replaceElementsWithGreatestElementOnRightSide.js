"use strict";
/**
 * @param {number[]} arr
 * @return {number[]} the same array but modified
 */

var replaceElements = function(arr) {
    let greatestValue = -1;
    for (let i = arr.length - 1; i >= 0; i--) {
        let temp = arr[i];
        arr[i] = greatestValue;
        if (temp > greatestValue) {
            greatestValue = temp;
        };
    };
    return arr;
};
//Testng
let arr = [17,18,5,4,6,1];
let arr1 = [400];
console.log(replaceElements(arr));