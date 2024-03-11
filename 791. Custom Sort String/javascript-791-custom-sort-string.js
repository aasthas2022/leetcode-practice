// Beats 97.85% of users with JavaScript

var customSortString = function(order, s) {
    let result = ''
    order_arr = Array.from(order)
    s_arr = Array.from(s)
    order_arr.forEach(element => {
        if(s.includes(element)) {
            let count = s.split(element).length - 1
            result += element.repeat(count)
        }
    });

    s_arr.forEach(element => {
        if(!result.includes(element)) {
            let count = s.split(element).length - 1
            result += element.repeat(count)
        }
    })

    return result
};


console.log(customSortString("cba", "abcdc"))