# Three sample lists
L1 = [1, 2, 3, 4, 5]
L2 = [5, 6, 7, 7, 8]
L3 = [8, 9, 0, 0, 5]

# Finding duplicates and stroing in one variable
common_elements = set(L1) & set(L2) & set(L3)

duplicate = list(common_elements)

# Printing the duplicate results
print("Duplicates:", duplicate)
