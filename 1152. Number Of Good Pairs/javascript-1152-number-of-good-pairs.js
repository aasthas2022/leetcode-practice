function numIdenticalPairs(nums){
    let good_pair_counter = 0
    for(let i=0; i < nums.length; i++) {
        for(let j=0; j<i; j++) {
            if(nums[i] === nums[j]) {
                good_pair_counter += 1
            }
        }
    }
    return good_pair_counter
}

console.log(numIdenticalPairs([1,2,3,1,1,3]))