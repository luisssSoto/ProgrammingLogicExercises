"use strict";

// Pascal's Triangle

/**
 * @param {int} rowIndex
 * @return {Array int} 
 * @author {Alex Soto}
 */

var pascalTriangle = function(rowIndex) {
    let rowPascal = [1];
    for (let i = 0; i < rowIndex; i++) {
        let n = rowPascal.length;
        rowPascal.unshift(0);
        rowPascal.push(0);
        for (let j = 0; j < n; j++) {
            rowPascal[j] = rowPascal[j] + rowPascal[j + 1];
        };
        rowPascal.splice(-1, 1);
    };
    return rowPascal;
};

// Testing
let rowIndex0 = 3;
let rowIndex1 = 0;
let rowIndex2 = 1;
console.log(pascalTriangle(rowIndex0));

// Complexity Analysis:
// Time Complexity: O(rowIndex2)
// Space Complexity: O(rowIndex)