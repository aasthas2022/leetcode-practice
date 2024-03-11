def numJewelsInStones(jewels, stones):
    counter = 0                                             # O(1)
    for letters_in_jewel in jewels:                         # O(n)
        for letters_in_stones in stones:                    # O(n) * O(n)
            if letters_in_jewel == letters_in_stones:       # O(1)
                counter += 1                                # O(1)
    return counter                                          # O(1)

print(numJewelsInStones('aA', 'aAAbbbb'))                  # Total time complexity : O(n^2)


def numJewelsInStones1(jewels, stones):
    
    counter = 0                                             # O(1)
    for stone in stones:                                    # O(n)
        if stone in jewels:                                 # O(1)
            counter += 1                                    # O(1)
    return counter                                          # O(1)

print(numJewelsInStones1('aA', 'aAAbbbb'))                  # Total time complexity: O(n)