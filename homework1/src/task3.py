# Create an if statement to check if a given number is positive,
# negative, or zero. Implement a for loop to print the first 10 prime numbers (you may need to
# research how to calculate prime numbers). Create a while loop to find the sum of all numbers from
# 1 to 100.

# Check if number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "positive"
    elif num == 0:
        return "zero"
    else:
        return "negative"


# Return first 10 prime numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def first_10_primes():
    primes = []
    # Set 1st prime num
    num = 2
    while len(primes) < 10:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


# Sum of numbers from 1 to 100
def sum_1_to_100():
    total = 0
    x = 1
    while x <= 100:
        total += x
        x += 1
    return total
