# Задача 2.
# Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих строках записаны
# N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Введите N: "))
my_list = []
for i in range(n):
    my_list.append(int(input("Введите элемент: ")))
x = int(input("Введите X: "))
min_value = abs(my_list[0]-x)
number = my_list[0]
for i in my_list:
    if x == i:
        number = i
        break
    else:
        value = abs(i-x)
        if value < min_value:
            min_value = value
            number = i
print(number)
