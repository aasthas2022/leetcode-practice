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

- **Javascript**:
    1. **Array Concatenation**:
        - Both methods demonstrate different approaches to concatenate arrays in JavaScript. 
        - The `concat()` method combines arrays by appending the elements of one array to another, while the spread operator `[...nums, ...nums]` achieves the same result by creating a new array with the elements of `nums` duplicated.
    2. **Spread Operator**:
        - The second method (`getConcatenation1`) showcases the usage of the spread operator (`...`) to spread the elements of the `nums` array into a new array. 
        - This operator provides a concise and readable way to manipulate arrays, offering flexibility and ease of use.
    3. **Functional Programming**:
        - Both functions follow a functional programming paradigm by not modifying the original array and instead returning a new concatenated array. 
        - This approach aligns with the principles of immutability, making the code more predictable and easier to reason about, especially in concurrent or asynchronous environments.

- **Python**:
    1. **Operator Overloading (`+`):**
        - In the `getConcatenation` method of `Solution` class, the `+` operator is overloaded for lists. 
        - When `nums + nums` is executed, it concatenates the two lists `nums` and `nums` together, effectively doubling the elements in the list.
    2. **List Mutation (`extend` method):** 
        - In the `getConcatenation1` method of `Solution1` class, the `extend` method is used to mutate the original list `nums`. 
        - By extending `nums` with itself using `nums.extend(nums)`, the elements of the list `nums` are appended to themselves, again effectively doubling the elements in the list.
    3. **List Replication (`*` operator):**
        - In the `getConcatenation2` method of `Solution2` class, the `*` operator is used for list replication. 
        - When `nums * 2` is executed, it replicates the elements of the list `nums` twice, effectively achieving the same result as concatenating the list with itself.
