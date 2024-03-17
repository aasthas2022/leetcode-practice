# 1. Two Sum - https://leetcode.com/problems/two-sum/description/

# Code

-  [Javascript](./javascript-1-two-sum.js)
- [Python](./python-1-two-sum.py)

# Approach 1
## Intuition
The first approach to solving the two-sum problem involves a brute-force method where we iterate through the array twice to find pairs of elements that sum up to the target value.

## Approach
1. **Nested Loop Iteration**: The algorithm uses a nested loop structure. The outer loop iterates over each element of the array, and the inner loop iterates over the elements before the current element. This allows us to compare each element with all the previous elements.
2. **Pair Sum Calculation**: For each pair of elements (nums[i] and nums[j]), where j < i, the algorithm calculates their sum. If the sum equals the target value, it adds the indices of the pair to the result list.
3. **Result Return**: The algorithm returns the list containing the indices of the pair that sums up to the target value.

## Complexity
- **Time complexity**: The nested loop structure leads to a time complexity of O(n^2), where n is the length of the input array nums.
- **Space complexity**: Since the algorithm only uses a constant amount of extra space (result list), the space complexity is O(1).

# Approach 2
## Intuition
The second approach utilizes a more efficient method by employing a dictionary to store the indices of the elements encountered so far. This allows us to find the complement of each element (the value needed to reach the target sum) in constant time.

## Approach
1. **Dictionary for Index Storage**: The algorithm initializes an empty dictionary, num_indices, to store the indices of the elements encountered.
2. **Iterative Search for Complement**: As the algorithm iterates through the array using enumerate, it calculates the complement needed to reach the target sum (complement = target - num). It then checks if this complement exists in the num_indices dictionary.
3. **Pair Identification**: If the complement exists in num_indices, it means that a pair is found. The algorithm returns the indices stored in the dictionary corresponding to the complement and the current index.
4. **Index Update in Dictionary**: If the complement doesn't exist, the algorithm adds the current element and its index to num_indices.
5. **No Pair Found**: If no pair is found after iterating through the entire array, the algorithm returns an empty list.
   
## Complexity
- **Time complexity**: The algorithm iterates through the array once, resulting in a time complexity of O(n), where n is the length of the input array nums.
- **Space complexity**: The algorithm utilizes additional space to store indices in the num_indices dictionary. In the worst case, where no pair is found, the space complexity is O(n).
