# Добавить в класс статикметод

class auto:
    brand = None
    age = 0
    color = None
    mark = None
    weight = None
    price = 0

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def birhday(self):
        self.age +=1
        print(self.age)

    @staticmethod
    def cost_reduction(price):
        return price-500 if price>1000 else price


price=int(input('Введите стоимость: '))
print('Сторгованная стоимость:', auto.cost_reduction(price))