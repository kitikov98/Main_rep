# *Сделать своё исключение и подключить к try/except

class MyError(Exception):
    pass



class calkul:
    NEPR_VVOD = 0 #буду считать количество неправильных вводов с значений

    @staticmethod
    def number(num):
        try:
            num = int(num)
        except ValueError:
            print('Неверные ввод, введеное значение будет равно 1')
            num = 1
            calkul.NEPR_VVOD +=1
        return num

    @classmethod
    def nepr_vvod(cls):
        try:
            if cls.NEPR_VVOD > 1:
                raise MyError
        except MyError:
                print(f'Вы ввели уже {cls.NEPR_VVOD} раз(а) неправильно')



    def summ(self, first, second):
        self.first = self.number(first)
        self.second = self.number(second)
        return f'сумма чисел {self.first + self.second}'

    def differ(self, first, second):
        self.first = self.number(first)
        self.second = self.number(second)
        return f'разность чисел {self.first - self.second}'

    def mult(self, first, second):
        self.first = self.number(first)
        self.second = self.number(second)
        return f'произведение чисел {self.first * self.second}'

    def divis(self, first, second):
        self.first =self.number(first)
        self.second = self.number(second)
        try:
            return float(self.first)/self.second
        except ZeroDivisionError as err:
            print('Невозможно выполнить деление на ноль --', err)
        return

    def degr(self, first, second):
        self.first = self.number(first)
        self.second = self.number(second)
        return f'возведение первого числа в степень равную второму числу {self.first ** self.second}'

    def udegr(self, first, second):
        self.first = self.number(first)
        self.second = self.number(second)
        if self.second % 2 == 0 and self.first > 0:
            try:
                return self.first ** (1 / self.second)
            except ZeroDivisionError as err:
                return f'корень нулевой степени равен бесконечности {err}'
        elif self.second % 2 == 1:
            save_num = self.first    # Ввел доп. переменную, которая сохранит значение первой переменной,
                                     # для того чтоб отрицательные числа не считало комплексным методом
            self.first = -self.first if self.first < 0 else self.first
            try:
                return self.first ** (1 / self.second) if save_num > 0 else -(self.first ** (1 / self.second))
            except ZeroDivisionError as err:
                return f'корень нулевой степени равен бесконечности {err}'
        else:
            return f'Вы пытаетесь извлечь корень чётной степени из отрицательного числа'


sda = calkul()

print(sda.udegr(-8,4))
print('_'*25)
print(sda.summ(11,34))
print('_'*25)
print(sda.differ("sd",123))
print('_'*25)
print(sda.mult(2,3))
print('_'*25)
print(sda.divis("sd",3))
print('_'*25)
print(sda.degr(6,8))
print('_'*25)
sda.nepr_vvod()
