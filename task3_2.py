# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
import math

testList = [2, 3, 4, 5, 6]

halfIndex = math.ceil(len(testList)/2)

result = [n * m for n, m in zip(testList[:halfIndex],
                              testList[:len(testList) - halfIndex - 1:-1])]
print(testList)
print(result)
