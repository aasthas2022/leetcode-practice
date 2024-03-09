def getCommon(nums1, nums2):
    common_items_in_list = set(nums1).intersection(nums2)
    if common_items_in_list:
        return min(list(common_items_in_list))
    return -1

print(getCommon([1,2,3],[2,5]))