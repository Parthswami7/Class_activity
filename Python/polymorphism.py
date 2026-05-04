class cat: 
    def __init__(self ,name ,age):
        self.name = name 
        self.age = age

    def make_sound(self):
        print("Meow")

class dog:
    def __init__(self , name, age):
        self.name = name 
        self.age = age

    def make_sound(self):
        print("Bark")

cat1 =cat("Dodo",7)
dog1 =dog("Rony",4)

cat1.make_sound()
dog1.make_sound()
print(cat1.age)
print(dog1.age)