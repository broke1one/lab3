import os

def createFile():
    file_name = "f_1"
    if os.path.isfile(file_name):
        print("Файл уже существует")
    else:
        with open(file_name, 'w') as file:
            data = input("Введите строку: ")
            file.write(data + "\n")
            file.close()
        
    
def viewFile(file_name):
    if os.path.isfile(file_name):
         with open(file_name) as file: 
             for line in file:
                 print(line)
    else:
        print("Файла  не существует, для начала создайте его")



def addDataToFile():
    if os.path.isfile("f_1"):
        with open("f_1", "a") as file:
            data = input("Введиту строку: ")
            file.write(data + "\n")
    else:
        print("Файла  не существует, для начала создайте его")


def deleteFile(file_name):
    if os.path.isfile(file_name):
          os.remove(file_name)
          print("файл удален")
    else:
        print("Файла  не существует, для начала создайте его")



def task():
    line_number = 1

    if os.path.isfile("f_1"):
        with open("f_1") as file:
            for line  in file:
                if line_number % 2 == 0:
                    data = line
                    with open("f_2", "a") as second_file:
                        second_file.write(data)
                line_number += 1
                file_name = "f_2"
            viewFile(file_name)
    else:
        print("Файла не существует, для начала создайте его")



while True:
    print("Выберите действие:\n1 - Создать файл\n2 - Добавить данные в конец файла\n3 - Просмотр файла\n4 - Удаление данных из файла\n5 - Задание\n0 - Выход из программы ")
    choice = input()
    if choice == "1":
        createFile()
    elif choice == "2":
        addDataToFile()
    elif choice == "3":
        file_name = "f_1"
        viewFile(file_name)
    elif choice == "4":
        while True:
            n = input("Выберите какой файл хотите удалить:\n1 - f_1\n2 - f_2\n0 - выход из меню\n")
            if n == "1":
                file_name = "f_1"
                deleteFile(file_name)
            elif n == "2":
                file_name = "f_2"
                deleteFile(file_name)
            elif n == "0":
                print("Возврат в пердыдущее меню\n")
                break
            else:
                print("Неверный выбор, повторите попытку:\n")
    elif choice == "5":
        task()
    elif choice == "0":
        print("До свидания")
        break
    else:
        print("Неверный выбор, попробуйте еще раз")

    