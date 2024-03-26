ROMAN_TO_INT = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


var romanToInt = function(s) {
    let result = 0;
    let prev_val = 0;
    for (let i = s.length - 1; i >= 0; i--) {
        let val = ROMAN_TO_INT[s[i]]
        prev_val > val ? result -= val : result += val
        prev_val = val
    }  
    return result
};

console.log(romanToInt("IV"))