import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

def input_shape():
    shape_type = input("Введите тип фигуры (круг, квадрат, треугольник): ").lower()
    if shape_type == "круг":
        radius = float(input("Введите радиус: "))
        return Circle(radius)
    elif shape_type == "квадрат":
        side = float(input("Введите длину стороны: "))
        return Square(side)
    elif shape_type == "треугольник":
        a = float(input("Введите сторону a: "))
        b = float(input("Введите сторону b: "))
        c = float(input("Введите сторону c: "))
        return Triangle(a, b, c)
    else:
        raise ValueError("Неизвестный тип фигуры")

def output_result(shape):
    print(f"Площадь: {shape.area()}")
    print(f"Периметр: {shape.perimeter()}")

import json

def save_to_file(shapes, filename="shapes.json"):
    with open(filename, "w") as file:
        json.dump([shape.__dict__ for shape in shapes], file)

def load_from_file(filename="shapes.json"):
    with open(filename, "r") as file:
        data = json.load(file)
    shapes = []
    for item in data:
        if "radius" in item:
            shapes.append(Circle(item["radius"]))
        elif "side" in item:
            shapes.append(Square(item["side"]))