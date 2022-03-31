def schet(spisok, slovar):
    for i in spisok:
        if i in slovar:
            slovar[i] += 1
        else:
            slovar[i] = 1


list = [1,4,5,6,4,4,2,1,2,5,1,5,2]
dict ={}
schet(list, dict)

for item in dict:
    print(f'{item}  {dict[item]};')
