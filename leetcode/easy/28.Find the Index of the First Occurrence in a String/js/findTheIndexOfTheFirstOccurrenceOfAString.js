/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 * @author AlexSoto
 */

// time complexity O(nm)
// Where n = lenght of haystack
// Where m = length o needle
// space complexity O(1)
var strStr = function(haystack, needle) {
    let n = haystack.length;
    let m = needle.length;
    for (let windowStart = 0; windowStart <= n - m; windowStart++) {
        for (let i = 0; i < m; i++) {
            if (needle[i] !== haystack[windowStart + i]) {
                break;
            };
            if (i === m - 1) {
                return windowStart;
            };
        };
    };
    return -1
};

// Testing
h = "sadbutsad"
n = "sad"

console.log(strStr(h, n))