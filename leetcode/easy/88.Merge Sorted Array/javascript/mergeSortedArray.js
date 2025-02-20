"use strict";
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */

// 1. edge cases n is equal to zero
// 2. create a var that works like index from nums2 
// 3. for through nums1 to assign a value from nums2[var]
// 4. sort the array burble method

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