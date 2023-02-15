# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def degree_digit(a, b):
    if b==1: 
        return a; 
    return a* degree_digit (a, b-1)

print("Введите число A:")
number_a = int(input())
print("Введите число B:")
number_b = int(input())
if (number_b <= 0):
    print("Число B некорректно")
degree = degree_digit(number_a, number_b)
print(f"Число A в степени В: {degree}")