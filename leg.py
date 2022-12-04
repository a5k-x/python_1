# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

lis = [2, 3, 5, 9, 3]

def getSum(lis: list):
    sum: int = 0
    for i in range(0,len(lis)):
        if (i % 2 != 0):
            sum += lis[i]
    return sum

print(getSum(lis))

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math

lis = [2, 3, 4, 5, 6]

def getPair(lis: list):
    result = []
    lenghtLis = len(lis)
    for i in range(0, math.ceil(lenghtLis/2)):
        result.append(lis[i] * lis[lenghtLis-i-1])
    print(result)    

getPair(lis)
