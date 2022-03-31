def factorial(element):
    if  element == 0:
        return 1
    else:
        return element * factorial(element-1)

chislo = int(input('Введите число факториала '))
print(factorial(chislo))
