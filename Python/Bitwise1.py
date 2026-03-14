def Evenodd( n):
    if (n ^ 1 == n + 1) :
        return True
    else:
        return False

number = int(input("Enter your number : "))

if Evenodd(number):
    print(number,"is Even.")
else:
    print(number,"is odd.")