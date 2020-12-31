class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)

p1 = Person("Julia", 17)
p1.myfunc()

class Testing:
    def __init__(anyObjectYouLike, kitty):
        anyObjectYouLike.kitty = kitty

    def randomfunc(abc):
        print("My favorite animal is a " + abc.kitty)

p2 = Testing("cat")
p2.randomfunc()
p2.kitty = "snake"
p2.randomfunc()

del p1.age

class Pass:
    pass

class Naming:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

"""
so basically you create objects in the start of the program
with def init, name the variables attached to the objects,
then write a function using the variables? i dont really get
this 
"""

x = Naming("David", "Bruce")
x.printname()

"""
is it like dividing a program within a program? just 
for clarity? and also to have it go away when youre done
"""

class Child(Naming):
    def __init__(self, fname, lname, year):
        Naming.__init__(self, fname, lname)
        #or super which makes it inherit everything not just init
        super().__init__(fname, lname)
        self.birthyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "born in ", self.birthyear)

x = Child("Julia", "Bruce", 2003)
x.welcome()