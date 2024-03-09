function numJewelsInStones(jewels, stones) {
    let counter = 0
    for(let i=0; i<jewels.length; i++){
        for(let j=0; j<=stones.length; j++) {
            if(jewels[i] == stones[j]) {
                counter += 1
            }
        }
    }
    return counter
}

console.log(numJewelsInStones('aA', 'aAAbbbb'))