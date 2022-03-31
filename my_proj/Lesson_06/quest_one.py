slovo = b'r\xc3\xa9sum\xc3\xa9'
print(slovo)

new_slovo = slovo.decode()
print(new_slovo)

slovo_latin = new_slovo.encode('Latin1')
print(slovo_latin)

slovo_decode = slovo_latin.decode('Latin1')
print(slovo_decode)
