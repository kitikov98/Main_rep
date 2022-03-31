# *Создать метакласс

class NewClass(type):
    def __init__(cls, name, base, attr):
        super().__init__(name, base, attr)
        cls.high_cost = int(input('First price: '))


class auto(metaclass=NewClass):
    def price_incr(self):
        self.high_cost += 500
        return f'New price: {self.high_cost}'



auti = auto()
print(auti.price_incr())