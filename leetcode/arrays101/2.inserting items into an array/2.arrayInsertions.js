"use strict";

// Create the array with a capacity of 5
let intArray = Array(5);
console.log(intArray.length);
console.log(typeof intArray);
console.log(intArray instanceof Array);
console.log(intArray);
console.log();

// Fill out the array
let len = 0; // this variable helps us to keep track of the elements which are inserted
for (let i = 0; i < intArray.length; i++) {
    intArray[len] = i;
    len ++;
};
console.log(intArray);
console.log(len);
console.log();

// Insert at the end
intArray[len - 1] = 10;
console.log(intArray);
console.log();

// Insert at the start
/* This is a linear time complexity: O(N), where N is the length of the Array
    due of that is very costly */
for (let i = intArray.length - 1; i > 0; i--) {
    intArray[i] = intArray[i - 1];
};
console.log(intArray);
intArray[0] = 'zero';
console.log(intArray);
console.log();

// Insert anywhere in the Array, for instance at 2 index
let desireIndex = 2;
console.log(len);
for (let i = len - 1; i > desireIndex; i-- ) {
    intArray[i] = intArray[i - 1];
};
console.log(intArray);
intArray[desireIndex] = 'one';
console.log(intArray);
