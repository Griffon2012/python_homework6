# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов, отличной от 0.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

testList = [1.1, 1.2, 3.1, 5, 10.01]
myList = list(filter(lambda x: x != 0,  list(
    map(lambda x: round(x - int(x), 2), testList))))

print(max(myList) - min(myList))
