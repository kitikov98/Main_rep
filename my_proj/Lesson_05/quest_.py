def proverka_natext(perem):
    a = perem
    if perem.isdigit() is True:
        return a
    else:
        print('вы ввели неверное значение', a)

def proverka_polozh(osnovnaya_func):
    def wrapper():
        a = osnovnaya_func()
        if a > 0:
            if a is float:
                print('Вы ввели десятичную дробь',a)
            else:
                print('Вы ввели положительноечисло',a)
        elif a < 0:
            if a is float:
                print('Вы ввели отрицательную десятичную дробь',a)
            else:
                print('Вы ввели отрицательное число',a)
        else:
            print('вы ввели нуль', a)
    return wrapper

def osnovnaya_func(a):

        if a > 0:
            if type(a) is float:
                print('Вы ввели десятичную дробь',a)
            else:
                print('Вы ввели положительное число',a)
        elif a < 0:
            if type(a) is float:
                print('Вы ввели отрицательную десятичную дробь',a)
            else:
                print('Вы ввели отрицательное число',a)
        else:
            print('вы ввели нуль', a)

def o3snovnaya_func(chislo):
    print(chislo)

osnovnaya_func(input('Введите число '))