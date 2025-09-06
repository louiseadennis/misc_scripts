from random import choice
import sys

arg = int(sys.argv[1])

number_list = []

for i in range(5, arg):
    for j in range(arg  - i):
        number_list.append(i + 1)
        
print(str(choice(number_list)))
        
