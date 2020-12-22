import re
collected = set()

def is_sentence(s):
    return None != re.match(r'[A-Z][a-z]*( [A-z][a-z]*,?)*\.', s)

print(is_sentence('a dog'))
print(is_sentence('A dog.'))

def calculate_factorial(n):
    p = 1
    i = 2
    while i <= n:
        p *= i 
        i += 1
    return p

def convert_f_to_c(f):
    """ this function converts fahrenheit to centigrade
    parameters: f is input in degrees fahrenheit
    return: output in degrees centigrade
    """
    return (f-32)*5/9

def convert_c_to_f(c):
    """ this function converts centigrade to fahrenheit
    parameters: c is input in degrees centigrade
    return: output in degrees fahrenheit
    """
    return (c*9)/5+32

help(convert_f_to_c)

print(convert_c_to_f(90))
print(convert_c_to_f(20))
print(convert_c_to_f(35))
print(convert_c_to_f(11))
print(convert_c_to_f(73))

print(convert_f_to_c(32))
print(convert_f_to_c(212))
print(convert_f_to_c(72))
print(convert_f_to_c(15))
print(convert_f_to_c(120))

print(calculate_factorial(1))
print(calculate_factorial(2))
print(calculate_factorial(3))
print(calculate_factorial(4))
print(calculate_factorial(5))

quit()

while True:
    i = input('What is your sentence: ')
    print(f"Got {i}")
    if 'quit' in i:
        break
    if len(i) < 10:
        print('Too short')
        continue
    if 'e' in i:
        print('Must not contain an e')
        continue
    if not is_sentence(i):
        print('re says it\'s not a setence')
        continue
    print(f"This may be a setence without an e \"{i}\"")
    if i in collected:
        print('Setence is a repeat')
        continue
    collected.add(i)
    if len(collected) == 5:
        print('Yea! You won!')
        collected.clear()
        continue
    print(f"set is currently {collected} len={len(collected)}")
