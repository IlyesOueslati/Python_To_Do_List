from asyncio import tasks


user_choice = -1

tasks = []



def show_tasks():
    task_index = 0 
    for task in tasks:
        print(task + " [" + str(task_index) + "]")
        task_index += 1


def add_task():
    task = input("Enter the content of the task: ")
    tasks.append(task)
    print("A task has been added!")      
    

def delete_task():
    task_index = int(input("Enter the index of the task to be deleted: "))

    if task_index < 0 or task_index > len(tasks) - 1:
        print("A task with this index does not exist")
        return

    tasks.pop(task_index)
    print("Task deleted!")



def save_tasks_to_file():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task+"\n")
    file.close()


def load_tasks_from_file():
    try:
        file = open("tasks.txt")

        for line in file.readlines():
            tasks.append(line.strip())
    
        file.close()
    except FileNotFoundError:
        return

load_tasks_from_file()


while user_choice != 5:
    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        add_task()



    if user_choice == 3:
        delete_task()    


    if user_choice == 4:
        save_tasks_to_file()




    print("")
    print("1. Show task")
    print("2. Add task")
    print("3. Delete task")
    print("4. Save your changes to the file")
    print("5. Exit")


    user_choice = int(input("Choose a number: "))
    print()