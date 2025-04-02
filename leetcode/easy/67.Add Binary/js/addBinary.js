"use strict";

/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */

var addBinary = function(a, b) {
    let decA = BigInt(`0b${a}`);
    let decB = BigInt(`0b${b}`);
    
    console.log(`dec a: ${decA}, dec b: ${decB}`);
    
    let result = decA + decB;
    console.log(result);
    console.log(typeof result);

    if (result === 0n) {
        return '0';
    }
    let str_bin = result.toString(2);
    return str_bin;
};


const test_a = "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101"
const test_b = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011";
console.log(addBinary(test_a, test_b));
