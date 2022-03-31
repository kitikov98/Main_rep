from datetime import datetime
import time

def func_decorat(func_one):
    def wraper():
        start_time = datetime.now()
        func_one()
        end_time = datetime.now()
        print('время работы функции', end_time - start_time)
    return wraper

@func_decorat
def func_one():
    time.sleep(2)
    print('Строка из символов на кирилице')

@func_decorat
def func_two():
    time.sleep(3)
    list_one=[i for i in range(1,13)]
    print(list_one)

func_one()
func_two()
