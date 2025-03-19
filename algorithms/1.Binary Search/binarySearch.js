"use strict";
// Binary Search

let binarySearch = function(arr, item) {
    let beginPoint = 0;
    let lastPoint = arr.length - 1;
    let middlePoint = 0;
    while (beginPoint <= lastPoint) {
        middlePoint = Math.floor((beginPoint + lastPoint) / 2)
        let guessItem = arr[middlePoint];
        if (guessItem === item) {
            return middlePoint;
        } else if (guessItem > item) {
            lastPoint = middlePoint - 1
        } else if (guessItem < item) {
            beginPoint = middlePoint + 1
        };
    };
    return null;
};
let a = [1,2,3,4,5,6,7,8,9,10];
console.log(binarySearch(a, 4));
console.log(7 / 2);
console.log(Math.floor(7 / 2));