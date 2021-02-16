from pprint import pprint
import string

def analyze_text(sentence):
    word_list = sentence.split()
    word_density = dict()
    letter_density = dict()
    length_density = dict()
    for word in word_list:
        word = word.translate(str.maketrans('', '', string.punctuation))
        word = word.lower()

        if word in word_density:
            word_density[word] += 1
        else:
            word_density[word] = 1

        word_length = len(word)

        if word_length in length_density:
            length_density[word_length] += 1
        else:
            length_density[word_length] = 1

        for c in word:
            if c in letter_density:
                letter_density[c] += 1
            else:
                letter_density[c] = 1
                
    return (word_list, word_density, length_density, letter_density)


while True:
    line = input("What is your sentence? ")
    word_list, word_density, length_density, letter_density = analyze_text(line)
    print(f"Word list is {word_list}")
    print(f"Word density is {word_density}")
    print(f"Length density is {length_density}")
    print(f"Letter density is {letter_density}")
