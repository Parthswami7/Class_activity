file = open("Parth.txt", "r")
print(file.read())
file.close()

parth = open("Parth.txt","w")
parth.write("Hi! I am Parth Swami")
parth.close()

Father = open("Parth.txt","a")
Father.write("I am a student of class 9th")
Father.close()