import pprint

class Persist:
    # def __new__(cls, arg1, arg2):
    #     print(f"Persist::__new__ arg1={arg1} arg2={arg2}")
    #     instance = super(Persist, cls).__new__(cls)
    #     return instance

    def __init__(self):
        print(f"Persist::__init__")
        self.data = {}

    def __del__(self):
        print(f"Persist::__del__")

    def __enter__(self):
        print(f"Persist::__enter__")
        return self
    
    def __exit__(self, type, value, tb):
        print(f"Persist::__exit__")
        return self

    def __repr__(self):
        print(f"Persist::__repr__")
        return pprint.pformat(self.data)

    def __str__(self):
        print(f"Persist::__str__")
        return pprint.pformat(self.data)

    #
    # Accessing class data through "[]"
    #
    def __getitem__(self, key):
        try:
            value = self.data[key]
            print(f"Persist::__getitem__ key={key} value={value}")
            return value
        except:
            print(f"Persist::__getitem__ key={key} undefined")
            return None

    def __setitem__(self, key, value):
        print(f"Persist::__setitem__ key={key} value={value}")
        self.data[key] = value

    #
    # Accessing class metadata through "p.x"
    #
    def __getattr__(self, key):
        value = super(Persist, self).__getattr__(key)
        print(f"Persist::__getattr__ key={key} value={value}")
        return value

    def __setattr__(self, key, value):
        print(f"Persist::__setattr__ key={key} value={value}")
        super(Persist, self).__setattr__(key, value)

    def __add__(self, other):
        print(f"Persist::__add__ self={self} other={other}")
        return self

    def __contains__(self, item):
        print(f"Persist::__contains__ self={self} item={item}")
        return item in self.data


# p = Persist()

# # y = p.x
# # print(y)
# # #p.x = "x attr"
# # #print(f"p.x = {p.x}")

# p[2] = 4

# print(p[2])

# print(p)

# p2 = p + 5

# print(p2)

# print(4 in p2)
# print(2 in p2)