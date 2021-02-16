from termcolor import colored
import pickle
import yaml
import json
import cbor2 as cbor
from pprint import pprint

# with open('file_to_create.txt', "a") as my_file:
#     my_file.write(colored('top of program\n', 'green'))
#     for i in range(4):
#         my_file.write(f"i is {i}\n")
#     my_file.write(colored('bottom of program\n', 'red'))
#     my_file.write('\007\n\n')

# with open('file_to_create.txt', 'r') as rd_file:
#     for cnt, line in enumerate(rd_file):
#         print(f"{cnt} {line}")
#         print()
#         print()

with open('file_to_create.cbor', "wb") as my_file:
    d = {
        'list': [
            { "p1": 1, "p2": "2"},
            { "x1": 1, "x2": 2}
        ],
        'second key': b'\x01\x02\x03abcdef',
        "third key is a float": 3.1416
    }
    cbor.dump(d, my_file)

print('after write')

with open('file_to_create.cbor', "rb") as rd_file:
    data = cbor.load(rd_file)
    pprint(data)

# for cnt,it in enumerate(range(2,20,2)):
#     print(cnt,it)

# print()

# lst = [ 'david', 'julia', 'robert']

# for it in lst:
#     print(it)

# print()

# d = { 'david': 'father', 'julia': 'daughter', 'robert': 'son' }

# for cnt,(key,value) in enumerate(d.items()):
#     print(cnt, key, value)

# for tup in enumerate(d.items()):
#     print(type(tup), tup)

# def foo(n):
#     for i in range(n):
#         print('before yield')
#         yield (i*10)

# def foo2(n):
#     return list(range(n))

# x = foo(5)

# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

#help(x)
# print(type(x))

# print(dir(x))
# print()

# x2 = foo2(5)

# print(type(x2))

# print(dir(x2))

# for i in foo(5):
#     print(i)