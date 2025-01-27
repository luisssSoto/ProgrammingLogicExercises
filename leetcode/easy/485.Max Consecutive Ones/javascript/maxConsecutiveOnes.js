"use strict";
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function (nums) {
    let countOnes = 0;
    let greatestSequence = 0;
    for (let index in nums) {
        if (nums[index] === 1) {
            countOnes++;
        };
        if (nums[index] === 0 || index == nums.length - 1) {
            if (countOnes > greatestSequence) {
                greatestSequence = countOnes;
                countOnes = 0;
            } else {
                countOnes = 0;
            };
        };
    };
    return greatestSequence;
};

//Testing 
let n = [1, 1, 0, 1, 1, 1]
console.log(findMaxConsecutiveOnes(n));


/*
1. Understand
2. Break it down
iterate the array
create a variable to count the greatest sequently 1s
create anothe to save the greatest value
if is 1 score a point if not set up to 0 again
if that score is greater than the current greatest sustitute the value
return the greatest variable
3. Plan your approach
4. Test your logic
 */