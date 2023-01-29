#Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Если число стоит посередине, умножить его на само себя.

array = list(map(int, input('Введи сколько хочешь чисел через пробел: ').split()))
print(f'Исходный массив: {array}')
result = [(lambda i: array[i] * array[len(array) - i - 1])(i) for i in range(int(len(array) / 2))]
for i, r in enumerate(result):
    print(f'Произведение {i + 1} пары равно {r}')
if len(array) % 2 == 1:
    print(f'Произведение последней пары {array[int(len(array) / 2)] ** 2} ')