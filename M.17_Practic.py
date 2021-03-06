# -*- coding: utf-8 -*-
"""
Created on Mon May  9 04:34:25 2022

@author: zbookuser

Напишите программу, которой на вход подается последовательность 
чисел через пробел, а также запрашивается у пользователя любое число.

В качестве задания повышенного уровня сложности можете выполнить 
проверку соответствия указанному в условии ввода данных.

Далее программа работает по следующему алгоритму:
    1. Преобразование введённой последовательности в список
    2. Сортировка списка по возрастанию элементов в нем 
    (для реализации сортировки определите функцию)
    3. Устанавливается номер позиции элемента, который меньше введенного 
    пользователем числа, а следующий за ним больше или равен этому числу.

При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, 
который был рассмотрен в этом модуле. Реализуйте его также отдельной функцией.

Подсказка
Помните, что у вас есть числа, которые могут не соответствовать заданному 
условию. В этом случае необходимо вывести соответствующее сообщение

"""
def sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx-1] > x:
            array[idx] = array[idx-1]
            idx -= 1
        array[idx] = x
    return

def findPosition(num_list, number):
    first = 0
    last = len(num_list)-1
    while first <= last:
        middle = first + (last - first) // 2
        if num_list[middle] < number <= num_list[middle+1]:
            return middle
        elif num_list[middle] < number:
            first = middle + 1
        else:
            last = middle - 1
    return -1

#array = [0,2,3,1,6,5,9,8,7]
array = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
try:   
    x = int(input("Введите любое число: "))
    sort(array)
    if (x < array[0])or(array[-1] < x):
        raise ValueError("ОШИБКА. Неверное значение:")
except ValueError as error:
    print(error)
    print("Значение находится за пределами последовательности")
else:
    print(array)
    print("Hомер позиции элемента, который меньше введенного пользователем числа: ", findPosition(array, x))


