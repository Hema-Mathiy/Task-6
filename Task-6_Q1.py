# Given data list
data = [10, 501, 22, 37, 100, 999, 87, 351]
# Initializing empty lists to store even and odd numbers
even_numbers = []
odd_numbers = []

for number in data:
    # Checking if the number is even
    if number % 2 == 0:
        # If even, add it to the even_numbers list
        even_numbers.append(number)
    else:
        # If odd, add it to the odd_numbers list
        odd_numbers.append(number)
# Printing the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
