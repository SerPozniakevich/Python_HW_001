# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from cmath import sqrt
from unittest import result


x1 = float(input("Введите Х1:"))
x2 = float(input("Введите Х2:"))
y1 = float(input("Введите Y1:"))
y2 = float(input("Введите Y2:"))

size_line = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (0.5)

print(type(size_line))
print(f"длина отрезка {format(size_line, '.2f')}")
