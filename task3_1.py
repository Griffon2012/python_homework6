# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих
# на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ:12

myList = [2, 3, 5, 9, 3]

sumElements = sum([n[1] if n[0] % 2 != 0 else 0 for n in enumerate(myList)])

print(myList)
print(sumElements)
