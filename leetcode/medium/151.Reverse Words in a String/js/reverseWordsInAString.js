"use strict";
// Reverse Words in a String

// Approach 1: Built-in methods
var reverseWords = function(s) {
    // remove leading and trailing spaces
    s = s.trim();
    // split by spaces and reverse
    let words = s.split(/\s+/).reverse();
    // join the words with a space
    return words.join(" ");
}

// Testing
let s0 = "   the      sky is blue   ";
console.log(reverseWords(s0));

// Complexity Analysis
// Time complexity: O(N), where N is the number of characters in the input string.
// Space complexity: O(N), to store the result of split by spaces.