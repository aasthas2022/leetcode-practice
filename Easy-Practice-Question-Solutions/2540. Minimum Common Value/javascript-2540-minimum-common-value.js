function getCommon(nums1, nums2) {
    let common_elem_in_list = nums1.filter(i => nums2.indexOf(i) > -1)
    if (!common_elem_in_list) {
        return -1
    }
    return Math.min(common_elem_in_list)
}

console.log(getCommon([1,2,3],[2,5]))

function getCommon1(nums1, nums2) {
    let index1 = 0;
    let index2 = 0;
    
    while (index1 < nums1.length && index2 < nums2.length) {
        if (nums1[index1] === nums2[index2]) {
            return nums1[index1];
        } else if (nums1[index1] < nums2[index2]) {
            index1++;
        } else {
            index2++;
        }
    }
    
    return -1;
}