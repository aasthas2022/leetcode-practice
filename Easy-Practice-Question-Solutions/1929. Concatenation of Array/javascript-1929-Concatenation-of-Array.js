/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    return nums.concat(nums)
};

var getConcatenation1 = function(nums) {
    return [...nums, ...nums]
};


console.log(getConcatenation([1,2,1]))
console.log(getConcatenation1([1,2,1]))
