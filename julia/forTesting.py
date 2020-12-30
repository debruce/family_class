#for loops print everything in a list/set/whatever
#if you want to stop it halfway through a thing use break
"""
colors = ["red", "blue", "green"]
for x in colors:
    print(x)
    if x == "blue":
        break

print(".")
#depending on where the print is you get different results

for x in colors:
    if x == "blue":
        break
    print(x)

print(".")
#continue skips a value

for x in colors:
    if x == "blue":
        continue
    print(x)

print(".")
#range function returns numbers, ends at specified number
#starts at zero unless specified before end value
#goes up by one unless specified after end value

for y in range(6):
    print(y)

print(".")
#use else in a for loop to do things after a loop is finished
#not used if ended by a break
#pass allows empty loops like a class

adj = ["heavy", "fluffy", "brown"]
pet = ["cat", "dog", "bunny"]

for x in adj:
    for y in pet:
        print(x, y)

"""


def myfunc():
    print("function time")
myfunc()

def func1(fname):
    print(fname + "Bruce")
func1("David")
func1("Robert")
func1("Julia")

def func2(color, item):
    print(color + " " + item)
func2("blue", "slippers")

def func3(*kids):
    print("The youngest child is " + kids[3])
func3("Clarisse", "Agatha", "Tillie", "Everett")

def func4(fruit1, fruit2, fruit3):
    print("The best fruit is " + fruit2)
func4(fruit1 = "apple", fruit2 = "cherry", fruit3 = "fig")

def func5(**name):
    print("Their last name is " +name["lname"])
func5(fname = "Pat", lname = "Watson")

def func6(state = "California"):
    print("I am from " + state)
func6("New York")
func6("South Carolina")
func6()
func6("Montana")

def func7(fruit):
    for x in fruit:
        print(x)
fruit = ["apple", "cherry", "fig"]
func7(fruit)

def func8(x):
    return 5 * x
print(func8(5))

def func9():
    pass

def recurs(k):
    if (k > 0):
        result = k + recurs(k - 1)
        print(result)
    else:
        result = 0
    return result
print("Recursion Ex. Results")
recurs(6)
#dont really understand how this works? ask

