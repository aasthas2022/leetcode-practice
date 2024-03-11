# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers - https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers

## Learnings:

### Javascript:
1. **Function Declaration with Arrow Function Syntax**: 
   The `var minPartitions = function(n) { ... }` line declares a function named `minPartitions` using the arrow function syntax (`=>`). This syntax is a concise way of defining functions in JavaScript, particularly useful for anonymous functions or function expressions.

2. **Variable Declaration Using `var`**:
   The `var` keyword is used to declare variables in JavaScript. In this code snippet, `max_num` and `num_arr` are declared using `var`. However, it's worth noting that `var` has function scope rather than block scope, which means variables declared with `var` are accessible throughout the whole function, not just within the block where they are defined.

3. **Spread Syntax (`...`)**:
   The spread syntax (`...`) is used to expand an iterable (like an array) into individual elements. In this code, `[...n+'']` spreads the string representation of `n` into an array of characters. This technique is often used to convert strings into arrays.

4. **Array `map` Method**:
   The `map` method is used to transform elements of an array. In this code, `num_arr.map(n=>+n)` iterates over each character in `num_arr` (which is an array of string digits), converting each character back to a number using the unary plus operator (`+`). This is a common way to convert a string representation of numbers into actual numeric values.

5. **Arrow Function**:
   Arrow functions (`=>`) are a concise way to write anonymous functions in JavaScript. In this code, `n => +n` is an arrow function that takes a single parameter `n` and returns `+n`, which coerces `n` into a number.

6. **Implicit Type Conversion**:
   JavaScript allows implicit type conversion, where values are automatically converted from one data type to another when needed. For example, when concatenating a string with a number, the number is automatically converted to a string. In this code, `n` is implicitly converted to a string when it's concatenated with an empty string (`''`).
