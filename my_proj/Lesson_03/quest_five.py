import random
zagadano = int(random.randint(1,10))
popitki = int(input('Выберите уровень своего везения, указав число попыток, где 10 - минимальный, 1 - максимальный '))
if not 1 <= popitki <= 10:
    popitki = 10
while True:
    chislo = int(input('Какое число от 1 до 10 загадал компьютер? '))
    if chislo == zagadano:
        print('Верно')
        break
    else:
        print('Неверно')
        popitki = popitki-1
        if popitki == 0:
            print(f'Верным числом было число {zagadano}')
            break
