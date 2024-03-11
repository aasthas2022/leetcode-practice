var minPartitions = function(n) {
    max_num = 0
    num_arr = [...n+''].map(n=>+n)
    return Math.max(...num_arr)
};


console.log(minPartitions(32))