"use strict";
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */

// Approaching 1: Merge and Sort
var merge = function (nums1, m, nums2, n) {
    if (n === 0) {
        return nums1;
    } else {
        let nums2Index = 0;
        for (let i = m; i < nums1.length; i++) {
            nums1[i] = nums2[nums2Index];
            nums2Index++;
        };
        let isSorted = false;
        while (isSorted === false) {
            isSorted = true;
            for (let i = 0; i < nums1.length; i++) {
                if (nums1[i] > nums1[i + 1]) {
                    isSorted = false;
                    let temp = nums1[i + 1];
                    nums1[i + 1] = nums1[i];
                    nums1[i] = temp;
                };
            };
        };
    };
    return nums1;
};
let nums1 = [4,5,6,0,0,0];
let m = 3;
let nums2 = [1, 2, 3];
let n = 3;
console.log(merge(nums1, m, nums2, n));

// Time complexity: O((n+m)log(n+m)).

// The cost of sorting a list of length x using a built-in sorting algorithm is O(xlogx). 
// Because in this case, we're sorting a list of length m+n, we get a total time complexity 
// of O((n+m)log(n+m)).

// Space complexity: O(n), but it can vary.

// Most programming languages have a built-in sorting algorithm that uses 
// O(n) space.

// Approach 2: Three Pointer Technique
var merge1 = function(nums1, m, nums2, n) {
    let pointer1 = m - 1;
    let pointer2 = n - 1;
    for (let pointer3 = m + n - 1; pointer3 >= 0; pointer3--) {
        if (pointer1 >= 0 && pointer2 >= 0) {
            nums1[pointer3] = nums1[pointer1] > nums2[pointer2] ? nums1[pointer1--] : nums2[pointer2--]
        } else if (pointer1 >= 0) {
            nums1[pointer3] = nums1[pointer1--]
        } else {
            nums1[pointer3] = nums2[pointer2--]
        };
    };
    return nums1;
};

// Testing
let n1 = [4,5,6,0,0,0];
let m11 = 3;
let n2 = [1, 2, 3];
let n22 = 3;
console.log(merge1(n1, m11, n2, n22));
// Complexity Analysis

// Time complexity: O(n+m).

// Same as Approach 2.

// Space complexity: O(1).

// Unlike Approach 2, we're not using an extra array.
