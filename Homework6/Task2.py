# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного 
# минимума и не больше заданного максимума)

print("Введите размер массива ")
num = int(input())
list_1 = []
for i in range(num):
    n = int(input('введите элемент: '))
    list_1.append(n)
min = int(input("Введите минимум:"))
max = int(input("Введите максимум:"))
list_i = []
for i in range(len(list_1)):
    if min<=list_1[i]<=max:
        list_i.append(i)
print (list_i)