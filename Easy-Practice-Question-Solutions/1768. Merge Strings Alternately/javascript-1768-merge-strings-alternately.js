var mergeAlternately = function(word1, word2) {
    let maxLength = Math.max(word1.length, word2.length)
    let result = ''
    for(let i=0; i<maxLength; i++){
        if (i < word1.length) {
            result += word1[i]
        }
        if (i < word2.length) {
            result += word2[i]
        }
    }

    return result
};


console.log(mergeAlternately("abc", "pqrs"))
