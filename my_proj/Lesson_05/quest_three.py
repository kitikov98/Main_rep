zadanniy_kortage = ('aassaa','dad','dfdf','slovo')
perevod_vstroku = filter(lambda chislo: chislo if chislo == chislo[::-1] else None, zadanniy_kortage)
print(list(perevod_vstroku))
