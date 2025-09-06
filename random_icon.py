from random import choice

number_list = []

for i in range(100):
    for j in range(100  - i):
        number_list.append(i + 1)
        
print(str(choice(number_list)))
        
