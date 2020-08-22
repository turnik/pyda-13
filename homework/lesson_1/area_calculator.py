from abc import abstractmethod
from math import sqrt, pi


class GeometricShape(object):

    @abstractmethod
    def calculate_area(self) -> float:
        raise NotImplemented('Method is not implemented')


class Triangle(GeometricShape):

    def __init__(self, a, b, c):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)

    def calculate_area(self) -> float:
        p = (self.__a + self.__b + self.__c) / 2
        return sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))


class Circle(GeometricShape):

    def __init__(self, radius):
        self.__radius = float(radius)

    def calculate_area(self) -> float:
        return pi * self.__radius ** 2


class Rectangle(GeometricShape):

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def calculate_area(self) -> float:
        return self.__x * self.__y


class ShapeHandler(object):

    @abstractmethod
    def handle_build_operation(self) -> GeometricShape:
        raise NotImplemented('Method is not implemented')


class TriangleHandler(ShapeHandler):

    def handle_build_operation(self) -> GeometricShape:
        a = float(input('Введите длину стороны A:'))
        b = float(input('Введите длину стороны B:'))
        c = float(input('Введите длину стороны C:'))
        return Triangle(a, b, c)


class CircleHandler(ShapeHandler):

    def handle_build_operation(self) -> GeometricShape:
        radius = float(input('Введите радиус окружности:'))
        return Circle(radius)


class RectangleHandler(ShapeHandler):

    def handle_build_operation(self) -> GeometricShape:
        x = float(input('Введите ширину прямоугольника:'))
        y = float(input('Введите высоту прямоугольника:'))
        return Rectangle(x, y)
