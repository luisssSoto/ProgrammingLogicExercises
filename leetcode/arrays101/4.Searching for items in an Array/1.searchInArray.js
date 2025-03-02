"use strict";
//linear search O(n)

var linearSearch = function(array, len, element) {
    // edge cases
    if (len === 0) {
        return false;
    }
    // linear search
    for (let i = 0; i < len; i++) {
        if (array[i] === element) {
            return true;
        };
    };
    return false;
};

// Use the function
let arr1 = [];
let leng = 0;
for (let i = 0; i < 6; i++) {
    console.log(leng);
    arr1[leng++] = i;
    console.log(leng);
};
console.log(arr1);
console.log(leng);
console.log();

console.log(linearSearch(arr1, leng, 3));
console.log(linearSearch(arr1, leng, 10));