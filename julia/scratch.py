class MyClass:
    def __init__(self, a, b):
        print(f"Hello from the constructor a = {a}, b = {b}")
        self.a = a
        self.b = b

    def __del__(self):
        print(f"Hello from the destructor a = {self.a}, b = {self.b}")

    def __enter__(self):
        print("Hello from enter")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Hello from exit")

    def show(self):
        print(f"Hello from show a = {self.a}, b = {self.b}")

with MyClass(4, 5) as m:
    m.show()

"""
with open('MyFile.txt', 'w') as f:
    f.write('My first print statement to a file \n')
    f.write('My second print statement to a file \n')
"""