numberSmallest = int(input("Enter a small number:"))
numberLargest = int(input("Enter a large number:"))

while(numberSmallest):
    numberP = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberP 

print("The HCF is:", numberLargest) 