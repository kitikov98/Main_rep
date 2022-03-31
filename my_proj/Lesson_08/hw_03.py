# *Для рассмотренного на уроке класса Circle реализовать метод производящий
# вычитание двух окружностей, вычитание радиусов произвести по модулю.
# Если вычитаются две окружности с одинаковым значением радиуса,
# то результатом вычитания будет точка класса Point.

import math
from task_01 import Point


class Circle(Point):
  radius = 0

  def __init__(self, radius, x=0, y=0):
    super().__init__(x, y)
    self.radius = radius

  def edge_distance_from_origin(self):
    return abs(self.distance_from_origin() - self.radius)

  def area(self):
    return math.pi * (self.radius**2)

  def circumference(self):
    return 2 * math.pi * self.radius

  def __eq__(self, other):
    return self.radius == other.radius

  def __str__(self):
    return 'Circle' + super().__str__()[5:-1] + f', radius: {self.radius})'

  def __add__(self, other):
    point = super().__add__(other)
    radius = self.radius + other.radius
    return Circle(radius, point.x, point.y)

  def __sub__(self, other):
      x = math.fabs(self.x - other.x)
      y = math.fabs(self.y - other.y)
      radius = math.fabs(self.radius-other.radius)
      return Point(x,y) if self.radius == other.radius else Circle(radius,x,y)



first_circle = Circle(2,2,2)
another_circle = Circle(5,8,6)
print(first_circle-another_circle)
