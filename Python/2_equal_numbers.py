number1 = int(input("Enter first number to compare:"))
number2 = int(input("Enter second number to compare:"))
def twonumberequal():
    if (number1 ^ number2) ==0: 
        print("Number are equal")
    else:
        print("Number are not equal")
