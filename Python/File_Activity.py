'''file.read() → reads entire file
file.read(12) → reads 12 characters
file.readline() → reads one full line
file.readlines() → reads all lines into a list'''
file = open("Parth.txt", "r")
print(file.read())
file.close()

file = open("Parth.txt", "r")
print(file.read(8))
file.close()

file = open("Parth.txt", "r")
print(file.readline())
file.close()

file = open("Parth.txt", "r")
print(file.readlines())
file.close()