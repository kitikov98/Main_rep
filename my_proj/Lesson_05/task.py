def func_decorat(func_one):
    def wraper():
        start_time = datetime.now()
        func_one()
        end_time = datetime.now()
        print('время работы функции', end_time - start_time)
    return wraper