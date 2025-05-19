"use strict";

/**
 * @param {number[]} heights
 * @return {number} amountIndexes
 */

// 1. burble sort new sortHeights
// 1.1. isItSorted = false
// 1.2 while isItSorted equal false ...
// isItSorted = true
// for i equal 0, while i < heights length...
// ... if heights[i] > heights[i + 1] ... isItSorted = false
// temp = heights[i] heights[i] = heights[i + 1], heights[i +1] = temp
// 2. countIndexes = 0
// 3. for heights
// 3.1 if heights[i] != sortedHeights[i]... countIndexes += 1
// 4. return countIndexes
var heightChecker = function(heights) {
    let sortedHeights = heights.slice();
    let isItSorted = false;
    console.log(sortedHeights);
    while (isItSorted === false) {
        isItSorted = true;
        for (let i = 0; i < sortedHeights.length - 1; i++) {
            if (sortedHeights[i] > sortedHeights[i + 1]) {
                isItSorted = false;
                let temp = sortedHeights[i];
                sortedHeights[i] = sortedHeights[i + 1];
                sortedHeights[i + 1] = temp;
            };
        };
    };
    let countIndexes = 0;
    for (let i = 0; i < sortedHeights.length; i++) {
        if (sortedHeights[i] !== heights[i]) {
            countIndexes++;
        };
    };
    console.log(sortedHeights);
    console.log(heights);
    return countIndexes;
};

let heights = [1,1,4,2,1,3];
console.log(heightChecker(heights));

var heightChecker = function(heights) {
    let sortedHeights = heights.slice().sort((a, b) => a - b);
    let countWrongStudentPlaces = 0;
    for (let i = 0; i < heights.length; i++) {
        if (heights[i] !== sortedHeights[i]) {
            countWrongStudentPlaces++;
        };
    };
    return countWrongStudentPlaces;
};

// Testing 
let dataTest1 = [5,1,2,3,4];
console.log(heightChecker(dataTest1));

/**Complexity Analysis:
 * Time Complexity: O(NlogN)
 * Space Complexity: O(N)
 */