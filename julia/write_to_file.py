from termcolor import colored

with open('file_to_create.txt', "a") as my_file:
    my_file.write(colored('top of program\n', 'green'))
    for i in range(4):
        my_file.write(f"i is {i}\n")
    my_file.write(colored('bottom of program\n', 'red'))
    my_file.write('\007\n\n')

with open('file_to_create.txt', 'r') as rd_file:
    for cnt, line in enumerate(rd_file):
        print(f"{cnt} {line}")
        print()
        print()