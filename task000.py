#  Задайте натуральное число N. Напишите программу, которая составит список простых делителей числа N.

n = int(input("Введи натуральное число: "))

factors = list(filter(lambda x: n % x == 0, range(2, n + 1)))
el_dividers = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), factors))

print(f"Все простые делители числа {n}:", el_dividers)
