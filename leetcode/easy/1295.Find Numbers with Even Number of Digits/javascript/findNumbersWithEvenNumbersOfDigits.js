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
console.log(findNumbers([555,901,482,1771]));

// 1️⃣ Understand the problem thoroughly: Take your time to read and understand the problem. Ask questions if anything is unclear. It's crucial to have a clear understanding of what needs to be solved before you begin.

// 2️⃣ Break it down into smaller parts: Divide the problem into smaller, manageable parts. This makes it easier to tackle and can help you see the solution more clearly.

// 3️⃣ Plan your approach: Think about different ways to solve the problem and choose the best approach. Draw diagrams, write pseudocode, or make a flowchart to visualize the solution.

// 4️⃣ Test your logic: Before you write any code, walk through your solution manually to ensure it works. This can help you catch any errors or logical flaws early on.