def first_non_repeating_element(nums):
    # Creating an empty dictionary to store the value
    element_count = {}

    # Loop through the list, counting the number of times each element appears
    for num in nums:
        element_count[num] = element_count.get(num, 0) + 1

    # Iterate through the list again to find the first non-repeating element
    for num in nums:
        if element_count[num] == 1:
            return num

    # If no non-repeating element is found, return None
    return None

# Sample data list
numbers = [1, 3, 5, 3, 7, 2, 5]
result = first_non_repeating_element(numbers)

if result is not None:
    print("The first non-repeating element is:", result)
else:
    print("No non-repeating element found in the list.")
