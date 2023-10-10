import os
def viewFile(file_name):
    if os.path.isfile(file_name):
        with open(file_name) as file:
            for line in file:
                print(line)
    else:
        print("Файла с уроками не существует")


def task(file_name):
   subject_totals = {}

   if os.path.isfile(file_name):
    with open(file_name) as file:
        for line in file:
            parts = line.strip().split(':')
            subject = parts[0].strip()
            lesson_parts = parts[1].split()
            total_lessons = 0

            for part in lesson_parts:
                count, _ = part.split('(')
                total_lessons += int(count)

            if subject in subject_totals:
                subject_totals[subject] += total_lessons
            else:
                subject_totals[subject] = total_lessons

        for subject, total_lessons in subject_totals.items():
            print(f"{subject}: {total_lessons}")
        else:
            print("Файла не существует")






file_name = "lessons.txt"
while True:
    print("1 - Просмотр списка\n2 - Задание\n0 = Выход из программы")
    choice = input("")
    if choice == "1":
        viewFile(file_name)
    elif choice == "2":
        task(file_name)
    elif choice == "0":
        print("до свидания")
        break
    else:
        print("Неверный выбор, повторите попытку")
