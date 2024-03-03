
function arrayFromPermutation(nums) {
    let result = []                         // O(1) - assiginging variables
    for(let i=0; i<nums.length; i++){       // O(n) - for loop until array len
        result.push(nums[nums[i]])          // O(1) - push and O(n) for each item that is being pushed
    }
    return result                           // O(1) - returning result
}

// Total time complexitiy = O(1) + O(n) + O (1) + O(n) + O(1) = 3 O(1) + 2 O(n) = O(n) 

console.log(arrayFromPermutation([0,2,1,5,3,4]))