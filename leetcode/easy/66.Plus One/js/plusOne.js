"use strict";
/**
 * @param {number[]} digits
 * @return {number[]}
 */

var plusOne = function(digits) {
    let strDigits = '';
    let bigIntDigits = 0n;
    let amountZeroes = digits.length - 1;
    digits.forEach(character => {
        strDigits += String(character);
    });
    bigIntDigits = BigInt(strDigits);
    bigIntDigits += 1n;
    strDigits = String(bigIntDigits);
    for (let i = 0; i < strDigits.length; i++) {
        digits[i] = Number(strDigits[i]);
    };
    return digits;
};

// Testing
let data1 = [1,2,3];
let data2 = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3];
console.log(plusOne(data2));
