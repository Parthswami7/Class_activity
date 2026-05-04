class Empolyee :
    def __init__ (self):
        print("Empolyee is created")
    def __del__ (self):
        print("Employee is deleted")
a = Empolyee()
del a 