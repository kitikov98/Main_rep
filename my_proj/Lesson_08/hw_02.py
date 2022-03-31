# Создать 2 класса truck и car, которые являются наследниками класса auto.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи «move» выводит
# надпись «attention», его реализацию сделать при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек.,
# затем выдаётся сообщение «load» и снова пауза 1 сек.
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
# метода move, после появления надписи «move» должна появиться надпись
# «max speed is <max_speed>». Создать по 2 объекта для каждого из классов
# truck и car, проверить все их методы и атрибуты.
import time
from hw_01 import auto

class track(auto):
    max_load = 0

    def __init__(self, max_load, brand, age, mark):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()


    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)

class car(auto):
    max_speed = 0

    def __init__(self, max_speed, brand, age, mark):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super().move()
        return print(f'max speed is {self.max_speed}')

supercar_01 = car(140,"Volvo",12,"s80")
supercar_01.move()
print('brand: ',supercar_01.brand)
supercar_01.color='green'
print('color: ',supercar_01.color)
supercar_01.weight=1800
print('weight: ',supercar_01.weight)
supercar_01.birhday()
print('age:', supercar_01.age)
supercar_01.stop()

print('-'*30)
supercar_02 = car(120,"Volvo",10,"s80")
supercar_02.move()
print('brand: ',supercar_02.brand)
supercar_02.color='yellow'
print('color: ',supercar_02.color)
supercar_02.weight=3000
print('weight: ',supercar_02.weight)
supercar_02.birhday()
print('age:', supercar_02.age)
supercar_02.stop()

print('-'*30)
suptruck_01=track(1255,"Volvo",32,"FH")
suptruck_01.move()
print('brand: ',suptruck_01.brand)
suptruck_01.color='blue'
print('color: ',suptruck_01.color)
suptruck_01.weight=6000
print('weight: ',suptruck_01.weight)
suptruck_01.birhday()
print('age:', suptruck_01.age)
suptruck_01.load()
suptruck_01.stop()

print('-'*30)
suptruck_02=track(1500,"Volvo",23,"FH")
suptruck_02.move()
print('brand: ',suptruck_02.brand)
suptruck_02.color='red'
print('color: ',suptruck_02.color)
suptruck_02.weight=7500
print('weight: ',suptruck_02.weight)
suptruck_02.birhday()
print('age:', suptruck_02.age)
suptruck_02.load()
suptruck_02.stop()