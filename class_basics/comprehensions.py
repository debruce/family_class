s = 'hello'

print(s)
print(type(s))

for c in s:
    print(c)
print()

s = [ 'h', 'e', 'l', 'l', 'o']


print(s)
print(type(s))

for c in s:
    print(c)
print()


s = ( 'h', 'e', 'l', 'l', 'o')


print(s)
print(type(s))

for c in s:
    print(c)
print()

s = { 'h':1, 'e':2, 'l':3, 'ls':4, 'o':5 }

print(s)
print(type(s))
print(s.keys())
print(s.values())
print(s.items())

for k,v in s.items():
    print(f"key={k} value={v}")
print()


a1,a2,a3 = (5, ('x', 'y'), [3.14, 2.718])
print(a1)
print(a2)
print(a3)

print()
comp = [ x*x for x in [ 1, 2, 3, 4]]
print(comp)

print()
comp = { 'key'+str(x):'value'+str(x) for x in [ 1, 2, 3, 4]}

# while True:
#     k = input('What is your key? ')
#     print(f"k is {k}, comp is {comp}")
#     if k in comp:
#         print(f"{k} = {comp[k]}")
#     else:
#         print(f"{k} is not a key for comp")
#         ask = input('Would you like to define it? ')
#         if ask == 'yes':
#             ask = input('What is the value? ')
#             comp[k] = ask


while True:
    print(comp)
    k = input('What is your key? ')
    try:
        print(f"{k} = {comp[k]}")
    except KeyError:
        print(f"{k} is not a key for comp")
        ask = input('Would you like to define it? ')
        if ask == 'yes':
            ask = input('What is the value? ')
            comp[k] = ask