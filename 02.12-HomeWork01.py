class Rectangle:
    def __init__(self, length, width):  # инит - принимает длину и ширину
        self.length = length
        self.width = width


    def find_area(self):                # метод - находит площадь
        print(self.length * self.width)


    def find_perimetr(self):            # метод - находит периметр
        print((self.length + self.width) * 2)


    def draw_rectangle(self):           # метод - рисует фигуру
        x = self.width
        while x != 0:
            print(" *  " * self.length)
            x -= 1


nurs_brat_kvadrat = Rectangle(5, 5)     # создаем объект класса  Rectangle
nurs_brat_kvadrat.find_area()           # вызываем метод класса Rectangle
nurs_brat_kvadrat.find_perimetr()       # вызываем метод класса Rectangle
nurs_brat_kvadrat.draw_rectangle()      # вызываем метод класса Rectangle
