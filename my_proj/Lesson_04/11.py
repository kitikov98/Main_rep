import time
from datetime import datetime

def time_func(fffc):
    for i in range(1, fffc+1):
        ffdfc = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        time.sleep(1)
        return ffdfc


fff = int(input('введите число временных промежутков '))
fsf = [print(time_func(fff)) for i in range(1, fff+1)]







