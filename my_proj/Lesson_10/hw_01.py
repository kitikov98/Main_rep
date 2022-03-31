# Сделать калькулятор

class calkul:

    def summ(self, first, second):
        self.first = first
        self.second = second
        return f'сумма чисел {self.first + self.second}'

    def differ(self, first, second):
        self.first = first
        self.second = second
        return f'разность чисел {self.first - self.second}'

    def mult(self, first, second):
        self.first = first
        self.second = second
        return f'произведение чисел {self.first * self.second}'

    def divis(self, first, second):
        self.first = first
        self.second = second
        return f'частное чисел {float(self.first)/self.second}'

    def degr(self, first, second):
        self.first = first
        self.second = second
        return f'возведение первого числа в степень равную второму числу {self.first ** self.second}'

    def udegr(self, first, second):
        self.first = first
        self.second = second
        return f'извлечение корня равному второму числу из первого числа {self.first ** (1/self.second)}'





sda = calkul()
print(sda.summ(2, 3))
print(sda.udegr(5, 3))
print(sda.degr(2, 4))
print(sda.divis(41, 3))

