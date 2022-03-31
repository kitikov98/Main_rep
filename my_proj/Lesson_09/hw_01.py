# Сделать свой класс данных

from dataclasses import dataclass

@dataclass
class Books:
    auther: str
    genre : str
    name : str
    edition : int
    price : int

dune=Books(auther='F.Herbert',genre='sci-fy',name='Dune',edition=250000,price=20)
hyperion=Books(auther='D.Simmons',genre='sci-fy',name='Hyperion',edition=250000,price=23)
print(dune)
