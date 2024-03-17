var twoSum = function(nums, target) {
    for(let i=0; i<nums.length; i++){
        for(let j=0; j<i; j++){
            if(nums[i]+nums[j] == target){
                return [j, i]
            }
        }
    }
    return []
};

// console.log(twoSum([2, 7, 11,15], 9))
// console.log(twoSum([3,2,4], 6))
// console.log(twoSum([3,3], 6))
// console.log(twoSum([3,2,3], 6))  

var twoSum1 = function(nums, target) {
    let varIndex = {}
    for (let i=0; i<nums.length; i++) {
        complement = target - nums[i];
        if (varIndex.hasOwnProperty(complement)) {
            return [varIndex[complement], i]
        }
        varIndex[nums[i]] = i
    }
    return []
}

console.log(twoSum1([2, 7, 11,15], 9))
console.log(twoSum1([3,2,4], 6))
console.log(twoSum1([3,3], 6))
console.log(twoSum1([3,2,3], 6))  