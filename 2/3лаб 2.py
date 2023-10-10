import os
def viewList(file_name):
    if os.path.isfile(file_name):
        with open(file_name) as file:
            for line in file:
                print(line)
    else:
        print("Файла со студентами не существует, создайте его")


def task(file_name):
    if os.path.isfile(file_name):
        students_score = {}
        with open(file_name) as file:
            for line in file:
                data = line.split()
                surname = data[0]
                scores = [int(x) for x in data[1:]]
                avarage_score = sum(scores) / len(scores)
                students_score[surname] = avarage_score
        for surname, avarage_score in students_score.items():
            if avarage_score >= 8:
                print(f"{surname} - {avarage_score}")
    else:
        print("файла со студентами не существует, для начала создайте его")



file_name = "students.txt"
while True:
    print("1 - Просмотр всех студентов\n2 - Студенты, чем средний балл выше 8\n0 - Выход из программы\n")
    choice = input("")
    if choice == "1":
        viewList(file_name)
    elif choice == "2":
        task(file_name)
    elif choice == "0":
        print("До свидания")
        break
    else:
        print("Неверный выбор, повторите попытку")