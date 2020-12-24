class MyClass:
    def __init__(self):
        print('hello from __init__')

    def __del__(self):
        print('hello from __del__')

    def __enter__(self):
        print('hello from __enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('hello from __exit__')



# with MyClass() as cls:
#     print("hello from with-block")

try:
    with MyClass() as cls:
        print("hello from with-block two")
        a = 1
        b = 0
        c = a / b
        #raise Exception("my exception")
        print("bottom of with-block two")
    print('after with statement')
except Exception as ex:
    print('caught an exception')
    print(ex)

print('after try/except')