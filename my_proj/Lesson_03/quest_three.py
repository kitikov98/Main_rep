name = input('Введите ваше имя ')
while True:
    vozrast=input('Введите ваш возраст ')

    if not vozrast.isdigit() or int(vozrast) <= 0:
        print('Ошибка, повторите ввод')
    elif int(vozrast) < 10:
        print(f'Привет, шкет {name}')
    elif  10 <= int(vozrast) <= 18:
         print('Как жизнь {0}'.format(name))
    elif 18 < int(vozrast) < 100:
        print('Что желаете %s'% (name))
    elif 100 <= int(vozrast):
        print(f'{name}, вы лжете - в наше время столько не живут...')
        continue
