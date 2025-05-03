"use strict";
/**
 * @param {number[]} nums
 * @return {number}
 */

var findNumbers = function(nums) {
    let countEvenNumbers = 0;
    for (let i = 0; i < nums.length; i++) {
        if (String(nums[i]).length % 2 === 0) {
            countEvenNumbers ++;
        };
    };
    return countEvenNumbers;
};

let n = [12,345,2,6,7896];
let n2 = [555,901,482,1771];
console.log(findNumbers(n2));

// 1️⃣ Understand the problem thoroughly: Take your time to read and understand the problem. Ask questions if anything is unclear. It's crucial to have a clear understanding of what needs to be solved before you begin.

// 2️⃣ Break it down into smaller parts: Divide the problem into smaller, manageable parts. This makes it easier to tackle and can help you see the solution more clearly.

// 3️⃣ Plan your approach: Think about different ways to solve the problem and choose the best approach. Draw diagrams, write pseudocode, or make a flowchart to visualize the solution.

// 4️ Test your logic: Before you write any code, walk through your solution manually to ensure it works. This can help you catch any errors or logical flaws early on.

// Approach 1: Extract digits
var findNumbers2 = function(nums) {
    let evenDigitCount = 0;
    nums.forEach(num => {
        let countDigits = 0;
        while (num !== 0) {
            countDigits += 1;
            num = Math.floor(num / 10);
        }
        if ((countDigits & 1) === 0) {
            evenDigitCount += 1;
        };
    });
    return evenDigitCount;
};

// Testing 
console.log(findNumbers2(n));
console.log(findNumbers2(n2));

// Complexity Analysis:
// Time complexity: O(N . log(M))
// When dividing an integer x by y, there can be at most O(log y(x)) divisions: O(log M)
// Where M is each num in nums
// Then we perform a loop of each num: O(N)
// Where N is nums
// Space complexity: We are using constant extra space. Hence, the space complexity is O(1).


// Approaching 4: Constraint Analysis
var findNumbers3 = function(nums) {
    let countEvenDigits = 0;
    nums.forEach(num => {
        if ((num >= 10 && num <= 99) || (num >= 1000 && num <= 9999) || (num === 100_000)) {
            countEvenDigits += 1;
        };
    });
    return countEvenDigits;
};

// Testing
console.log(findNumbers3(n));
console.log(findNumbers3(n2));

// Complexity Analysis:
// Time complexity: O(N)
// Space complexity: O(1)