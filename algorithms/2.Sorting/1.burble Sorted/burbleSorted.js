"use strict";

/**
 * Bubble Sort Algorithm
 * @param {number[]} arr - The array to be sorted
 * @return {number[]} - The sorted array
 */
function bubbleSort(arr) {
    let n = arr.length - 1;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap the elements
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    return arr;
}

// Example usage:
let testData = [64, 34, 25, 12, 22, 11, 90];
let testData1 = [2,3,2,5,5,5,1,8,2,4,11];
console.log("Unsorted array:", testData1);
let sortedData = bubbleSort(testData1);
console.log("Sorted array:", sortedData);