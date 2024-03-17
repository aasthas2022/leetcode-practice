var isPalindrome = function(x) {
    if (x.toString() == x.toString().split("").reverse().join("")){
        return true
    }
    return false
};

console.log(isPalindrome(121))