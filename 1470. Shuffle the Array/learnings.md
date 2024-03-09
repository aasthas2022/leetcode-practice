# 1470. Shuffle the Array - https://leetcode.com/problems/shuffle-the-array

## Javascript:

- Reiteration on what I learned.

## Python:

### Zip:
- **Definition**:
  - `zip` is a built-in Python function that takes two or more iterables (like lists, tuples, etc.) and returns an iterator that aggregates elements from each iterable.

- **Usage**:
  - It iterates over the iterables in parallel.
  - At each iteration, it returns a tuple containing the corresponding elements from each iterable.

- **Example**:
  ```python
  list1 = [1, 2, 3]
  list2 = ['a', 'b', 'c']
  zipped = zip(list1, list2)
  for pair in zipped:
      print(pair)  # Output: (1, 'a'), (2, 'b'), (3, 'c')
  ```

### Slicing:
- **Definition**:
  - Slicing is a technique in Python used to extract a portion of a sequence (like a list or string) by specifying a start index, end index, and an optional step size.

- **Usage**:
  - It provides a concise way to work with segments of sequences without modifying the original sequence.
  - Slicing can be used on lists, tuples, strings, and other sequence types in Python.

- **Example**:
  ```python
  my_list = [1, 2, 3, 4, 5]
  sliced_list = my_list[1:4]  # Extracts elements from index 1 to 3 (exclusive)
  print(sliced_list)  # Output: [2, 3, 4]
  ```

