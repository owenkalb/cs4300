# If statement to see if number is positive or negative or zero
# Validate input
while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input!")
# Check if pos
if num > 0:
    print("The number is positive")
# Check if zero
elif num == 0:
    print("The number is zero")
else:
# Check if neg
    print("The number is negative")

# For loop to print first 10 prime numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("\nThe first 10 prime numbers")
counter = 0
# Start with first prime number
num = 2
# loop for the first 10 prime numbers
while counter < 10:
    if is_prime(num):
        print(num)
        counter += 1
    num += 1


# While loop to find sum of all numbers from 1 to 100
print("\nSum of all numbers from 1-100")
x=1
temp = 0
while x<101:
   temp = temp + x
   x = x + 1
# Print sum
print(temp) 
