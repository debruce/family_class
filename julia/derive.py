class Base:
    def __init__(self):
        print("hello from Base::__init__")

    def __del__(self):
        print("hello from Base::__del__")

    def method(self):
        print("hello from Base::method")

class Derived(Base):
    def __init__(self):
        print("hello from Derived::__init__")

    def __del__(self):
        print("hello from Derived::__del__")

    def method(self):
        print("hello from Derived::method")
        super(Derived, self).method()


def test_base():
    print("before Base")
    b = Base()
    b.method()
    print("after Base")


def test_derived():
    print("before Derived")
    d = Derived()
    d.method()
    # d.method2()
    print("after Derived")

# test_base()
# print("\nafter test_base\n")

test_derived()
print("\nafter test_derived\n")