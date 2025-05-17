// Find All Numbers Disappeared In An Array
var findAllNumbers = function(nums) {
    let uniqueNums = new Set(nums);
    let missingNums = [];
    for (let i = 1; i <= nums.length; i++) {
        if (!(uniqueNums.has(i))) {
            missingNums.push(i);
        };
    };
    return missingNums;
};
let dataTest0 = [1,1];
console.log(findAllNumbers(dataTest0));