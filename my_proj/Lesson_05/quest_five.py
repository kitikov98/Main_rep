def prov_str(func):
    def wraper(simv):
        first_simv = simv
        simv = simv.replace('-', '', 1)
        simv = simv.replace(',', '', 1)
        simv = simv.replace('.', '', 1)
        if simv.isdigit() is False:
            print('Вы ввели не корректное число: ', first_simv)
        else:
            func(first_simv)
    return wraper


def prov_otr(func):
    def wraper(simv):
        if '-' in simv:
            print(f'Вы ввели отрицательное {func(simv)} число:', simv)
        else:
            print(f'Вы ввели положительное {func(simv)} число:', simv)
    return wraper


@prov_str
@prov_otr
def prov_float(simv):
    if '.' in simv:
        return 'дробное'
    elif ',' in simv:
        return 'дробное'
    else:
        return 'целое'


rita_name = input('введите строку ')
prov_float(rita_name)
