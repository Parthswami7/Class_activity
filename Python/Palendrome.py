a = int(input("Enter an number:"))
b = a
r = 0 
while a > 0 :
    c = a % 10 
    r = r * 10 + c
    a //= 10 

if b == r :
    print("it is an palilndrome.")
else :
    print("it is not a palilndrome.")