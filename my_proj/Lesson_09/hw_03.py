# Добавить в класс классметод

class book_shop:
    Names : str
    amount_inshop = 5
    price = 12
    amount_sell =0

    def __init__(self):
        book_shop.amount_sell += 1
        book_shop.amount_inshop -= 1

    @classmethod
    def income(cls):
        return print(f'Today i selled {book_shop.amount_sell} book, my total incom {book_shop.price*cls.amount_sell}') if cls.amount_inshop >= 0 else print(f'all books are sold, come back later')


book1= book_shop()
book1.income()

book2= book_shop()
book2.income()

book3= book_shop()
book3.income()
book4= book_shop()
book4.income()
book5= book_shop()
book5.income()
book6= book_shop()
book6.income()
book7= book_shop()
book7.income()


