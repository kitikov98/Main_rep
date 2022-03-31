# более длинная комбинация
# должна проверяться раньше
# чтоб всякой хуйни не было


stroka=input('введите предложение')
if 'codec' in stroka:
    print('Yes, 2')
elif 'code' in stroka:
    print('Yes, 1')
else:
    print('No')