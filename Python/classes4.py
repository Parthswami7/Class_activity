class Parrot:
    species = "bird"
    def __init__ (self,name,age):
        self.name = name
        self.age = age 
    def sing(self,song):
        return "{} sings {}".format(self.name, song)
    def dance(self):
        return "{} is now dancing".format(self.name)
a = Parrot("Blu", 10)
print(a.sing("happy"))
print(a.dance())