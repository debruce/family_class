#!/usr/local/bin/python3
 
import sys

class Base:
    def __init__(self):
            print("Base::__init__")

    def __del__(self):
        print("Base::__del__")

    def __enter__(self):
        print("Base::__enter__")
        return self

    def __exit__(self, type, value, tb):
        print("Base::__exit__")
        #return True
        
    def raiser(self):
        raise RuntimeError("raised my error")

class Derived(Base):
    def __init__(self):
            print("Derived::__init__")
            super(Derived, self).__init__()

    def __del__(self):
        print("Derived::__del__")

    def __enter__(self):
        print("Derived::__enter__")
        return self

    def __exit__(self, type, value, tb):
        print("Derived::__exit__")
        #return True

try:
    with Derived() as d:
        print('top of body')
        d.raiser()
        print('bottom of body')
except:
    print(f"try block caught {sys.exc_info()}")