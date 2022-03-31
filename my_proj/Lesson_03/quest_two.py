name = input('Введите ваше имя ')
while True:
    vozrast = input('Введите ваш возраст ')

    if not vozrast.isdigit() or int(vozrast) <= 0:
        print('Ошибка, повторите ввод')
        continue

    if int(vozrast) < 10:
        print(f'Привет, шкет {name}')
        break
    elif 10 <= int(vozrast) <= 18:
        print('Как жизнь {0}'.format(name))
        break
    elif 18 < int(vozrast) < 100:
        print('Что желаете %s' % name)
        break
    else:
        print(f'{name}, вы лжете - в наше время столько не живут...')
