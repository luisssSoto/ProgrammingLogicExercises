"use strict";
// Longest Common Prefix

/**
 * 
 * @param {Array strings} strs 
 * @returns {string}
 * @author {Alex Soto}
 */

// Approach 1: Horizontal Scanning
var longestCommonPrefix = function(strs) {
    if (strs.length === 0) {
        return ""
    };
    let prefix = strs[0]
    for (let i = 1; i < strs.length; i++) {
        while (strs[i].indexOf(prefix) != 0) {
            prefix = prefix.slice(0, prefix.length - 1); 
            if (prefix === "") {
                return ""
            };
        };
    };
    return prefix;
};

// Complexity Analysis
// Time complexity : O(S) , where S is the sum of all characters in all 
// strings.
// Space complexity : O(1). We only used constant extra space.