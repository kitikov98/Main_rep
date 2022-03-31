stroka = input('Введите произввольную строку')
nechetn_stroka = stroka[0::2]
chetn_stroka = stroka[1::2]
stroka = stroka.strip()
print('введённая строка', stroka,end="\n\n\n")

print(nechetn_stroka,chetn_stroka,sep="     ",end="!!!\n")
