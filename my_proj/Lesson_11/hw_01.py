# Создать генератор геометрической прогрессии

def geom_progr(num,shag=1):
    while True:
        num*=shag
        yield print(f'Значение прогрессии в данный момент: {num}')


dsd = geom_progr(-3, -3)
next(dsd)
next(dsd)
next(dsd)
next(dsd)
next(dsd)

