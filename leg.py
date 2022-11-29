# 1) Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Введите число = : "))
array = []
def getMultiply(n):
    multiply = 1    
    for i in range(1, n+1):
        multiply *= i
        array.append(multiply)  

getMultiply(n)
print(array) 

#2) Требуется найти наименьший натуральный делитель
#  целого числа N, отличный от 1.
  
n = int(input("Введите число = : "))
def getMinDel(n):
    k = 2
    flag = False
    while (flag == 0):
        if (n % k == 0):
            flag = True
            print(k)
        else:
            k +=1
getMinDel(n) 

#3) Задайте список из (2*N+1) элементов, заполненных числами из 
# промежутка [-N, N]. Найдите произведение элементов на указанных ИНДЕКСАХ.
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

n = abs(int(input("Введите число = : ")))
a = []
def getArray(n):
    m = n * -1
    for m in range(m, n+1):
        a.append(m)
        a.reverse
getArray(n)
print(a)

randomArray = [2, 2, 3, 1, 8]
def findMultiply(array: list):
    k = 1
    for i in range(0, len(array)):
        k *=array[i]
    return k
print("Произведение элементов произвольного списка =", findMultiply(randomArray))