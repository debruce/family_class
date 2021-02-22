import sys
from termcolor import colored, cprint

sys.stderr.write('this is stderr\n')
sys.stderr.flush()
sys.stdout.write('this is stdout\n')
print(sys.argv)

def main(arg):
    print(arg)

main(sys.argv[1])

var1 = 70
var2 = 'chrissy'
var3 = "A kissaroo from me to you"

'''
print(sys.getsizeof(var2))
print(sys.maxsize)
print()
'''

print(colored(f"{var3}", 'magenta', "on_blue"))