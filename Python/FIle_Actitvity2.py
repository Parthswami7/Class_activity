file = open("Parth.txt", "r")
file1 = open("Parth1.txt", "w")
for i in file.readlines():
    if not(line.startswith("Coding")):
        print(i)
        file1.write(i)

file.close()
file1.close()