# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# def degree(a, b, c):
#     if b == 0:
#         return c
#     return degree(a, b - 1, c * a)

# a = int(input("Введите число возводимое в степень: "))
# b = int(input("Степень числа: "))
# c = a
# print(f"Ваше число {a} в степени {b} равно {degree(a, b, c)}")



# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# def sum(a, b):
#     a += 1
#     b -= 1
#     if b > 0:
#         return sum(a, b)
#     return a
# a = int(input("Введите 1-ое число: "))
# b = int(input("Введите 2- ое число: "))
# print(f"Сумма введенных вами чисел равна {sum(a, b)}")