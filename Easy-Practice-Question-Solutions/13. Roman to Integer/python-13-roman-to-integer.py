ROMAN_TO_INT = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def romanToInt(s: str):
    result = 0
    prev_val = 0
    for letter in s:
        val = ROMAN_TO_INT[letter]
        if val < prev_val:
            result -= val
        else:
            result += val
        prev_val = val
            
    return result
    
print(romanToInt("III"))
print(romanToInt("LVIII"))


'''
- Traverse through each letter of string
- if letter is key of roman_to_int obj, add the value to result
- return result
'''