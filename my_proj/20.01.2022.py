list_odin = [1, 34, 5]
list_dva = [33, 12, 10]
print(list_odin)
print(list_dva)
list_odin.insert(0, 20)
list_odin.append(21)
list_dva.insert(0, 134)
list_dva.append(321)
print(list_odin)
print(list_dva)
list_odin.extend(list_dva)
print(list_odin)

listodin =(1,3)
listdva = [1,2]
dictodin = {listodin: listdva}
print(dictodin)
dictdva = {tuple(listdva): listodin}
print(dictdva)

