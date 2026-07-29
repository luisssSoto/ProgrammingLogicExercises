"use strict";

// Create an array with a length of 10
let myArray = new Array(10);
console.log(myArray);
console.log(myArray.length);
console.log();

// Fill out the first 6 slots in the array
let len = 0; // this variable keeps track each insertion or deletion you make
for (let i = 0; i < 6; i++) {
    myArray[i] = i;
    len++;
};
console.log(myArray);
console.log();

// Delete at the end of the array (least costly)
// This not to delete any element but you can insert any element at the last slot by
// using it like an index
len--;
myArray[len] = 'last element';
console.log(myArray);
console.log();

// Delete from the start of the array (O(N) time complexity ) is the most costly
for (let j = 0; j < len; j++) {
    myArray[j] = myArray[j + 1];
};
len--; // Don't forget to keep up-to-date this variable
console.log(myArray);
myArray[len] = ' ';
console.log(myArray);
console.log();

// Delete from anywhere (O(K) time complexity where K is the elements on the right)
// But like is probably that K will be equal to the start we can say also that is O(N)
// Delete at 3th index
for (let k = 2; k < len; k++) {
    myArray[k] = myArray[k + 1];
};
len--;
console.log(myArray);