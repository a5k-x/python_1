# 1) Вычислить число Pi c заданной точностью d, не используя ф. round()

import math

'''d = abs(int(input("С какой точностью вывести число ПИ? ")))

def getPi(d: int):
    mnogitel = 10 ** d 
    return int(math.pi * mnogitel) / mnogitel

print(getPi(d))'''

# 2) Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной
#  последовательности.(Вывод тех элементов, которые были без повторов)

d: list[int] = [1, 2, 3, 2, 4, 4, 8, 8]
a = []
def getUnique(list: list[int]):
   unique = {i for i in list if list.count(i) <= 1}
   print(unique)
   
getUnique(d)

print(a)