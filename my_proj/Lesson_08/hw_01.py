# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран «move» и «stop»,
# а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.


class auto:
    brand = None
    age = 0
    color = None
    mark = None
    weight = None

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birhday(self):
        self.age +=1
        print(self.age)

if __name__ == '__main__':
    mycar = auto('lada',12,'vesta')
    mycar.move()
    mycar.stop()
    mycar.birhday()