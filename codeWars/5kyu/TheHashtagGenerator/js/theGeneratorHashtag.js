"use strict";

var generatorHashtag = function(str) {
    str = str.trim();
    if (str.length === 0) {
        return false;
    };
    str = str.split(" ");
    str = str.map(word => {
        return word.charAt(0).toUpperCase() + word.slice(1);
    });
    str = str.join("");
    str = "#" + str;
    if (str.length > 140 || str.length === 0) {
        return false;
    };
    return str;
};

// Testing
let s0 = " Hello there thanks for trying my Kata      ";
let s1 = "    Hello     World   ";
let s2 = "     ";
console.log(generatorHashtag(s2));

// Complexity Analysis:
// Time Complexity: O(N) where N is the length of the array
// Space Complexity: O(1)
