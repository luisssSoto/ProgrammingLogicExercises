"use strict";
/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in place instead.
 */

// 1. for iterate arr 
// 2. if zero, it goes into second for
// 3. for shift all the elements since that position one slot to the right
// 4. repeat step one but it the last for was executed start from 1 slot more
var duplicateZeros = function(arr) {
    for (let i = 0; i < arr.length; i++) {
        if(arr[i] === 0) {
            for (let j = arr.length - 1; j > i; j--) {
                arr[j] = arr[j - 1];
            };
            i++;
        };
    };
    return arr;
};

let dataTestInput = [[1,0,2,3,0,4,5,0], [1,2,3]];
let dataTestOutput = [[1,0,0,2,3,0,0,4], [1,2,3]];

// Testing
import { assert } from 'chai';
describe('Testing Duplicate Zeros', function() {
    for (let i = 0; i < dataTestInput.length; i++) {
        it('should returns the modified array', () => {
            let input = [...dataTestInput[i]]; // Create a copy of the input array
            duplicateZeros(input); // Modify the copy in place
            console.error(`INPUT: ${input}\nOUTPUT: ${dataTestOutput[i]}`);
            assert.strictEqual(JSON.stringify(input), JSON.stringify(dataTestOutput[i]), 'The set of arrays don\'t match');
        });
    };
});