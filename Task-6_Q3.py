# Defining a function to check if a number is a happy number
def happy_num(num):
    seen_numbers = set()
    while num != 1 and num not in seen_numbers:
        # Adding the current number to the set
        seen_numbers.add(num)
        # Replacing the number with the sum
        num = sum(int(digit) ** 2 for digit in str(num))
        # Returns If the number becomes 1
    return num == 1
# Given data list
data = [10, 501, 22, 37, 100, 999, 87, 351]

happy_numbers = [num for num in data if happy_num(num)]
# Printing the results
print("Happy numbers are:", happy_numbers)
print("Count of happy numbers:", len(happy_numbers))
