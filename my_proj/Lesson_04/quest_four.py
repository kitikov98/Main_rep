import time
from datetime import datetime

def time_func(kol_vo):
    for i in range(1, kol_vo+1):
        vremya = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        time.sleep(1)
        return vremya


promezh = int(input('введите число временных промежутков '))
spisok = [time_func(promezh) for i in range(1, promezh+1)]
print(spisok)