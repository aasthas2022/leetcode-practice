function defangIPaddr(address) {
    return address.replaceAll(".", "[.]") // O(1)
}

console.log(defangIPaddr("1.1.1.1"))