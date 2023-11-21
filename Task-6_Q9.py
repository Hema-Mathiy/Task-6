from itertools import combinations
# Defining a function to find triplets
def triplets(L, key):
    # Defining a helper function to check if the sum of a triplet is equal to the key
    def valid(val):
        return sum(val) == key
    return list(filter(valid, list(combinations(L, 3))))

# Given data lists
L = [10, 20, 30, 9]
key = 59

# Print the results
print(triplets(L, key))
