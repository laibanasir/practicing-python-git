class rectangle: 
    def __init__(self, length, width):
        self.width = width
        self.length = length
    def area(self):
        area = self.length * self.width
        print('Area of the rectangle :', area)
    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print('Perimeter of the rectangle :', perimeter)

first_rect = rectangle(2, 7)
second_rect = rectangle(7, 12)

rectangle.area(first_rect)
rectangle.perimeter(first_rect)

rectangle.area(second_rect)
rectangle.perimeter(second_rect)
