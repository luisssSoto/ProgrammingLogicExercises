"use strict";

// Longest Substring Without Repeating Characters

/**
 * 
 * @param {string} s
 * @return {number} 
 */
var longestSubstring = function(s) {
    let beginWin = 0;
    let endWin = 0;
    let subStr = "";
    let greatestLen = 0;
    while (endWin < s.length) {
        if (!subStr.includes(s[endWin])) {
            subStr += s[endWin];
        } else if (subStr.includes(s[endWin])) {
            greatestLen = Math.max(subStr.length, greatestLen);
            let itWasFound = false;
            while (itWasFound === false) {
                if (s[beginWin] === s[endWin]) {
                    itWasFound = true;
                };
                beginWin++;
            };
            subStr = s.slice(beginWin, endWin);
            subStr += s[endWin];
        };
        endWin++;
    };
    greatestLen = Math.max(subStr.length, greatestLen);
    return greatestLen;
};

let s0 = "abcabcbb";
let s1 = "bbbbb"
let s2 = "pwwkew"
let s3 = " "
let s4 = "au"
let s5 = "bbtablud";
console.log(longestSubstring(s5));
s0 = s0.slice(1, s0.length);
console.log(s0);