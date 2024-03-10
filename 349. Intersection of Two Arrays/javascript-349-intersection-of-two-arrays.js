var intersection = function(nums1, nums2) {
    let common_elem = []
    nums1.forEach(element => {
        if(nums2.includes(element) && !common_elem.includes(element)){
            common_elem.push(element)
        }  
    });

    return common_elem
    
};


console.log(intersection([1,2,2,1], [2,2]))


var intersection1 = function(nums1, nums2) {
    const set1 = new Set(nums1)
    const set2 = new Set(nums2)
    let common_elem = []
    set1.forEach(element => {
        if(set2.has(element)){
            common_elem.push(element)
        }  
    });

    return common_elem
    
};


console.log(intersection1([1,2,2,1], [2,2]))