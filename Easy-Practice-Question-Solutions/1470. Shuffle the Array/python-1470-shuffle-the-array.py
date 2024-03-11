def shuffle(nums, n):
    result = []
    arr_1 = nums[0:n]
    arr_2 = nums[n:2*n]
    for i, j in zip(arr_1, arr_2):
        result.append(i)
        result.append(j)
    return result

print(shuffle([2,5,1,3,4,7], 3))