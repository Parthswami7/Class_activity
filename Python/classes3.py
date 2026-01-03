class Parrot:
    species = "bird"
    def __init__  (self,name,age):
        self.name = name
        self.age = age
a = Parrot("Blu", 10)
b = Parrot("Woo", 15)

print(a.name)
print(a.age)

print(b.name)
print(b.age)


print("Blu is a {}".format(a.species))

print("Woo is also a {}".format(b.species))

print("{} is {} years old".format(a.name, a.age))

print("{} is {} years old".format(b.name, b.age))