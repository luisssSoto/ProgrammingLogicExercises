"use strict";
/**
 * @param {number} numRows
 * @return {number [][]}
 * @author Alex Soto
 */

var generate = function(numRows) {
    let mainArray = [[1]];
    for (let i = 0; i < numRows - 1; i++) {
        let tempArray = mainArray[mainArray.length - 1].slice()
        tempArray.unshift(0);
        tempArray.push(0);
        let subArray = [];
        for (let j = 0; j < tempArray.length - 1; j++) {
            let newElement = tempArray[j] + tempArray[j + 1];
            subArray[j] = newElement;
        };
        mainArray.push(subArray);
    };
    return mainArray;
};

// Testing
let numRow = 5;
let expected1 = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]];
console.log(generate(numRow));