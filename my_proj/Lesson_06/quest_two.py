str_one = input('Строка 1: ')
str_two = input('Строка 2: ')
str_three = input('Строка 3: ')
str_four = input('Строка 4: ')

new_f = open('quest_two.txt', 'w')
new_f.write(str_one+'\n')
new_f.write(str_two+'\n')
new_f.close()

with open('quest_two.txt', 'a') as new_f:
    new_f.write(str_three+'\n')
    new_f.write(str_four+'\n')

