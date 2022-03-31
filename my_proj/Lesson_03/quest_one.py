predlozhenie = input('введите предложение из двух слов ').split()
slovo_one = predlozhenie[0]
slovo_two = predlozhenie[1]
slovo_one, slovo_two = slovo_two, slovo_one
print('!%s ! %s!' % (slovo_one, slovo_two))
print('!{0} ! {1}!'.format(slovo_one, slovo_two))
print(f'!{slovo_one} ! {slovo_two}!')
