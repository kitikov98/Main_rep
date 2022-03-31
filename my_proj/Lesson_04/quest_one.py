dic_one = {'key': 2, 'quest': 4, 'lesson': 7}
dic_two = {value: key for key, value in dic_one.items()}
print(dic_two)