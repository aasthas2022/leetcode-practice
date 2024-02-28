# [2703. Return Length of Arguments Passed]( https://leetcode.com/problems/return-length-of-arguments-passed/description/)

### Description
Write a function `argumentsLength` that returns the count of arguments passed to it.

### Example
```javascript
Input: args = [5]
Output: 1
Explanation:
argumentsLength(5); // 1
```
One value was passed to the function so it should return 1.

```javascript
Input: args = [{}, null, "3"]
Output: 3
Explanation: 
argumentsLength({}, null, "3"); // 3
```
Three values were passed to the function so it should return 3.
 
### Constraints

- `args` is a valid JSON array
- 0 <= args.length <= 10

## Learnings:

- **Python**:
     - In Python, the asterisk * is used for unpacking iterable objects like lists, tuples, or sets into separate elements. 
     - When used in function definitions, it allows a function to accept a variable number of arguments.
     - In the context of function definitions, *args collects any number of positional arguments passed to the function into a tuple. 
     - This means that you can call the function with any number of arguments, and they will all be collected into the args tuple.

- **Javacript**:
    - In JavaScript, prior to the introduction of the rest parameter syntax (...args), if you wanted a function to accept a variable number of arguments, you would typically use the arguments object, which is an array-like object accessible inside functions that contains all the arguments passed to the function. 
    - However, arguments is not a true array, so it lacks array methods like forEach, map, etc.
    - The rest parameter syntax provides a more convenient and concise way to work with variable numbers of arguments by allowing you to represent an indefinite number of arguments as an array.
    - Here's how the rest parameter syntax works:
        1. When you define a function with a rest parameter, you use three dots (...) followed by a parameter name (in this case, args). 
        2. This parameter will collect all remaining arguments passed to the function and package them into an array.
        3. Within the function body, you can treat args as an array, even though it's not explicitly defined in the function signature. 
        4. You can use array methods like length, forEach, map, etc., directly on args.
        5. When calling the function, you can pass any number of arguments, and they will be collected into the args array.