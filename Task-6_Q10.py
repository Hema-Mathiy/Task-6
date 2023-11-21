def sublist(arr, l):
    for i in range(l - 1):
        s = arr[i]  # Initializing the sum with the current element
        for j in range(i + 1, l):
            s += arr[j]  # Adding the current element to the sum
            # Checking if the sum is equal to zero
            if s == 0:
                return True

    # If no sub-list with a sum equal to zero is found
    return False
# Given data list
list = [4, 2, -3, 1, 6]

# Checking if there is a sub-list with a sum equal to zero
result = sublist(list, len(list))

# Print the result
if result:
    print("There is a sub-list with sum equal to zero.")
else:
    print("No sub-list with a sum equal to zero.")
