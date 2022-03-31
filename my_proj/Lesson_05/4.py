def bread(func):
  def wraper():
    print("<------->")
    func()
    print("<_______>")

  return wraper


def ingredients(func):
  def wraper():
    print("#помидор#")
    func()
    print("~салат~")

  return wraper


@bread
@ingredients
def sandwich(food="--ветчина--"):
  print(food)

print(sandwich())