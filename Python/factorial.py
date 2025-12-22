<<<<<<< HEAD
# Python program to check if a number is prime
# Take input from the user
num = int(input("Enter a number: "))

# Check if number is greater than 1 (since primes are > 1)
if num > 1:
    # Loop only up to the square root of num for efficiency
    for i in range(2, int(num**0.5) + 1):
        # If num is divisible by any number, it's not prime
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    # If no divisors were found, the number is prime
    else:
        print(f"{num} is a prime number.")
else:
    # Numbers less than 2 are not prime
    print(f"{num} is not a prime number.")
=======
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def divide(x,y):
    return x/y

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))


print(add(num1,num2))

print(sub(num1,num2))

print(mul(num1,num2))

print(divide(num1,num2))
>>>>>>> 027272f30868ad8287a548ca8b6d123252cbd15c
