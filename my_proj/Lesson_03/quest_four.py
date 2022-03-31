chislo=int(input('Введите число '))
schet = 1
summa = 0
while chislo >= schet:
    summa = summa + schet**3
    schet +=1
print(f'Сумма кубов {summa}')

summa_for = 0
for schet_for in range(1, chislo+1):
    summa_for=summa_for+schet_for**3

print(f'Сумма кубов {summa_for}')