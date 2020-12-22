print("Enter as many unique sentences as possible without the letter e.")
incorrect = 0
correct = 0
import sys

first = input("First: ")
if "e" in first:
    incorrect += 1
elif len(first) <= 10:
    print("A full sentence, please")
    sys.exit()
else: 
    correct += 1

second = input("Second: ")
if "e" in second:
    incorrect += 1
elif second == first :
    print("Unique sentences, please.")
    sys.exit()
elif len(second) <= 10:
    print("A full sentence, please.")
    sys.exit()
else:
    correct += 1

third = input("Third: ")
if "e" in third:
    incorrect += 1
elif third == first:
    print("Unique sentences, please.")
    sys.exit()
elif len(third) <= 10:
    print("A full sentence, please.")
    sys.exit()
elif third == second:
    print("Unique sentences, please.")
    sys.exit()
elif len(third) <= 10:
    print("A full sentence, please.")
    sys.exit()
else:
    correct += 1

fourth = input("Fourth: ")
if "e" in fourth:
    incorrect += 1 
elif fourth == first:
    print("Unique sentences, please.")
    sys.exit()
elif len(fourth) <= 10:
    print("A full sentence, please.")
    sys.exit()
elif fourth == second:
    print("Unique sentences, please.")
    sys.exit()
elif len(fourth) <= 10:
    print("A full sentence, please.")
    sys.exit()
elif fourth == third:
    print("Unique sentences, please.")
    sys.exit()
elif len(fourth) <= 10:
    print("A full sentence, please.")
    sys.exit()
else:
    correct += 1

fifth = input("Fifth: ")
if "e" in fifth:
    incorrect += 1
elif fifth == first: 
    print("Unique sentences, please.")
    sys.exit()
elif len(fifth) <= 10:
    print("A full sentence, please.")
    sys.exit()
elif fifth == second:
    print("Unique sentences, please.")
    sys.exit()
elif len(fifth) <= 10:
    print("A full sentence, please.")
    sys.exit()
elif fifth == third:
    print("Unique sentences, please.")
    sys.exit()
elif len(fifth) <= 10:
    print("A full sentence, please.")
    sys.exit()
elif fifth == fourth:
    print("Unique sentences, please.")
    sys.exit()
elif len(fifth) <= 10:
    print("A full sentence, please.")
    sys.exit()
else:
    correct += 1

if incorrect > 0:
    print("Nice try, but there was an e in there.")
else:
    print("Congratulations, no e's!")