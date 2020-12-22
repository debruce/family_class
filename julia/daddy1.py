import re
collected = set()

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
    if not re.match(r'[A-Z][a-z]*( [A-z][a-z]*,?)*\.', i):
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
