pi = 3.14
class circle:
    def __init__(self, rad):
        self.rad = rad
    def area(self):
        area = pi * self.rad ** 2
        print('Area of the circle :', area)
    def perimeter(self):
        perimeter = 2 * pi * self.rad
        print('Perimeter of the circle :', perimeter)

cirlce_first = circle(3)
cirlce_first.area()
cirlce_first.perimeter()

circle_second = circle(7)
circle_second.area()
circle_second.perimeter()