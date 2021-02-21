user_choice = -1

tasks = []


def show_tasks_with_number():
    task_index = 1
    for task in tasks:
        print(str(task_index) + ". " + task)
        task_index +=1
    print("---")
    print()

def add_task():
    task = input("Wpisz tresc zadania: ")
    tasks.append(task)
    print("zadanie zostało dodane")

def delete_task():
    task_index = int(input("Podaj numer zadania"))

    if task_index < 0 or task_index > len(tasks) - 1:
        print("No such action")
        return

    tasks.pop(task_index)
    print("Action removed")

def save_to_file():
    file = open("Globe.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()

def load_tasks_from_file():
    file = open("Globe.txt")

    for line in file.readlines():
        tasks.append(line.strip())
    file.close()



load_tasks_from_file()
while user_choice < 5:
    if user_choice == 1:
        show_tasks_with_number()

    if user_choice == 2:
        add_task()

    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        save_to_file()


    print("1. Show actions")
    print("2. Add action")
    print("3. Remove action")
    print("4. Save to file")
    print("5. Quit")

    user_choice = int(input("Choose number: "))