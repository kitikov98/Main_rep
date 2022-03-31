#функция isdigit() проверяет, состоит ли
# строка только из цифр.


stroka = input('введите возраст ')


if not stroka.isdigit() or int(stroka) <= 0:
    print('Wrong input')
elif int(stroka) <= 12:
    print('Orange')
elif int(stroka) < 18:
    print('CocaCola')
else:
    print('Beer')