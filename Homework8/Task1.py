# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# 1. Вывод всех контактов
# 2. Поиск контакта
# 3. Добавить контакт (сразу сохрорнять в файл)
# 6. Выход по требованию пользователя

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
# функционал для изменения и удаления данных

import os
file_dir = os.path.dirname(os.path.realpath(__file__))
file_name = f"{file_dir}/Phone_numbers.txt"

def view_contacts():
    with open(file_name, "r", encoding="utf8") as data:
        for line in data:
            print(line.replace("\n", ""))

def find_contact(word:str):
    with open(file_name, "r", encoding="utf8") as data:
        for line in data:
            if word.upper() in line.upper():
                print(line)

def add_contact(new_contact):
    with open(file_name, "a", encoding="utf8") as data:
        data.write("\n"+new_contact)

def change_contact(word:str):
    buffer = ""
    with open(file_name, "r", encoding="utf8") as data1:
        lines = data1.readlines()
        for line in lines:
            line = line.strip()
            if word.upper() in line.upper():
                print (line)
                new_contact = str(input("Введите новый контакт:"))
                buffer += new_contact+'\n'
            else:
                buffer += line+'\n'
    with open(file_name, 'w', encoding="utf8") as data2:
        data2.write(buffer)

def delete_contact(word:str):
    buffer = ""
    with open(file_name, "r", encoding="utf8") as data1:
        lines = data1.readlines()
        for line in lines:
            line = line.strip()
            if word.upper() not in line.upper():
                buffer += line+'\n'
    with open(file_name, 'w', encoding="utf8") as data2:
        data2.write(buffer)

def main_menu():
    while True:
        num = int(input('Введите: 1 - печать справочника;'
            ' 2 - поиск контакта; 3 - добавить контакт; 4 - изменить контакт;'
            ' 5 - удалить контакт; 6 - выйти из программы: '))
        if num == 1:
            view_contacts()
        elif num == 2: 
            find_contact(str(input("Введите слово:")))
        elif num == 3:
            add_contact(str(input("Введите контакт:")))
        elif num == 4:
            change_contact(str(input("Введите контакт:")))
        elif num == 5:
            delete_contact(str(input("Введите контакт:")))
        elif num == 6:    
            break
        
main_menu()