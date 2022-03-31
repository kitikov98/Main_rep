while True:
    input_value = input('введите число: ')

    if not input_value.isdigit():
        continue

    print(f'Куб введенного чисда = {int(input_value) ** 3}')

    answer = input('Хотите выйти из приложения, (Y/Д)')
    if answer.upper() in ('Y', 'Д'):
        break
