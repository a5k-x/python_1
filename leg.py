# 1) Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

numberDay = abs(int(input("Введите день недели: ")))

def checkDayOfWeek(numberDay):
    if (numberDay > 0 and numberDay < 6): print("Нет")
    if (numberDay > 6 and numberDay < 8): print("Да")
    else: print("Не правильно указанное число")

checkDayOfWeek(numberDay)
print("\n")

# 2) Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#в которой находится эта точка (или на какой оси она находится).

x = int(input("Введите X = : "))
y = int(input("Введите Y = : "))

def getNumberPlateQuater(x, y):
    if (x > 0 and y > 0): print(1)
    if (x < 0 and y > 0): print(2)
    if (x < 0 and y < 0): print(3)
    else: print(4)

getNumberPlateQuater(x, y)

# 3) Напишите программу, которая принимает на вход координаты двух 
# точек и находит расстояние между ними в 2D пространстве.

import math

x0 = int(input("Введите X0 = : "))
y0 = int(input("Введите Y0 = : "))

x1 = int(input("Введите X1 = : "))
y1 = int(input("Введите Y1 = : "))

def getDistance(x0,y0, x1, y1):
    return math.sqrt( ((x1 - x0)**2) + ((y1 - y0)**2))

print(getDistance(x0, y0, x1, y1))    