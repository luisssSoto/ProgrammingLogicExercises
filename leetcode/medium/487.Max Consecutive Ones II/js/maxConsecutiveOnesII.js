// Max Consecutive Ones II
/**
 * @param {Array int} nums
 * @returns {int} 
 * @author {Alex Soto}
 */
var maxConsecutiveOnesII = function(nums) {
    let rightPointer = 0;
    let leftPointer = 0;
    let amountZeroes = 0;
    let longestSequence = 0;
    while (rightPointer < nums.length) {
        if (nums[rightPointer] === 0) {
            amountZeroes++;
        };
        while (amountZeroes === 2) {
            if (nums[leftPointer] === 0) {
                amountZeroes--;
            };
            leftPointer++;
        };
        if (rightPointer - leftPointer + 1 > longestSequence) {
            longestSequence = rightPointer - leftPointer + 1;
        };
        rightPointer++;
    };
    return longestSequence;
};

// Testing
let dataTest3 = [1,0,0,1,1,0,1];
console.log(maxConsecutiveOnesII(dataTest3));

/**
 * Complexity Analysis
Let n be equal to the length of the input nums array.

Time complexity : O(n). Since both the pointers only move forward, 
each of the left and right pointers traverse a maximum of n steps. 
Therefore, the time complexity is O(n).

Space complexity : O(1).
We don't store anything other than variables. 
Thus, the space we use is constant because it is not correlated to 
the length of the input array.
 */