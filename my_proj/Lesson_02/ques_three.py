chislo_odin = (560, 'aa', 12, 10)
chislo_dva = (560, 'aa', 12, 10)
chislo_tri = (560, 'aa', 12, 10)
print(chislo_odin, chislo_dva, chislo_tri, id(chislo_odin), id(chislo_dva), id(chislo_tri))

chislo_odin = list(chislo_odin)
chislo_dva = list(chislo_dva)
chislo_tri = list(chislo_tri)
print(chislo_odin, chislo_dva, chislo_tri, id(chislo_odin), id(chislo_dva), id(chislo_tri))

permen_odin = [1, 12, 34]
permen_dva = [1, 12, 34]
print(permen_odin, permen_dva, id(permen_odin), id(permen_dva))


print(id(tuple(permen_odin)), id(tuple(permen_dva)))

