# [1920. Build Array from Permutation](https://leetcode.com/problems/build-array-from-permutation/)

# [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/description/)

### Description
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.

### Example 1:
```
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
```

### Example 2:
```
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
```

### Constraints:
- n == nums.length
- 1 <= n <= 1000
- 1 <= nums[i] <= 1000

## Learnings:

- **JavaScript**:
    - **Time Complexity**: The function `arrayFromPermutation` iterates over each element of the `nums` array once, resulting in a time complexity of O(n), where n is the length of `nums`.
    - **Space Complexity**: It creates a new array `result` to store the result, leading to a space complexity of O(n).
    - **Variable Assignment**: Initialization of variables like `result` occurs efficiently with a time complexity of O(1).
    - **Array Manipulation**: The `push` method adds elements to `result` with a time complexity of O(1) per operation, resulting in O(n) overall due to the loop.
    - **Total Time Complexity**: The dominant operation, the loop iterating over `nums`, determines the function's total time complexity, which is O(n).

- **Python**:
    - **Time Complexity**: The `arrayFromPermutation` function iterates over each element of the `nums` list once using a for loop, resulting in a time complexity of O(n), where n is the length of `nums`.
    - **Space Complexity**: It creates a new list `result` to store the result, leading to a space complexity of O(n).
    - **List Manipulation**: The `append` method adds elements to `result` with an amortized time complexity of O(1) per operation.
    - **Total Time Complexity**: The dominant operation, the loop iterating over `nums`, determines the function's total time complexity, which is O(n).
    - **Function Invocation**: Invoking the `print` function to display the result does not significantly impact the overall time complexity of the `arrayFromPermutation` function.
