'''file.read() → reads entire file
file.read(12) → reads 12 characters
file.readline() → reads one full line
file.readlines() → reads all lines into a list'''
file = open("Parth.txt", "r")
print(file.read())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
for i in file:
    print(i)
file.close()

file = open("Parth.txt","w")
file.write(" File in write mode ....")
file.write("Hi! I am Penguin. I am 1 yr. old")
file.close()

file = open("Parth.txt", "a")
file.write("\n File in append mode ....")
file.write("Hi! I am Penguin. I am 1 yr. old")
file.close()

file = open("Parth.txt","r")
print(file.read())