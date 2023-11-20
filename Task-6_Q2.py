# Defining a function to check the number is prime or not
def is_prime(num):
    # Verifying the numbers are not prime by checking if they are less than or equal to 1.
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    # Checking the divisibility starting from 5
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    # If no divisors are found, the number is prime
    return True
# The given List to check the prime number
data = [10,501,22,37,100,999,87,351]

prime_numbers = [num for num in data if is_prime(num)]
# Printing the result
print("Prime numbers is", prime_numbers)
print("Count of prime numbers:", len(prime_numbers))
