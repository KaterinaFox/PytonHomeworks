# Задача 1
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
print ('Введите количество элементов первого множества:')
n = int(input())
print ('Введите количество элементов второго множества:')
m = int(input())
my_list1 = set()
for i in range(n):
   my_list1.add(int(input("Введите элемент 1-го множества:")))
my_list2 = set ()
for i in range(m):
   my_list2.add(int(input("Введите элемент 2-го множества:")))

my_list_int = my_list1.intersection(my_list2)
if len(my_list_int) == 0:
    print("множества не пересекаются") 
else:
    print (f'--> {my_list_int}')