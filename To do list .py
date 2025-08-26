#To do list

todo_list = []
 
 # Menu 
def show_menu():
    print("\n_To Do List Menu_") 
    print("1) View Tasks")
    print("2) Add Task")
    print("3) Remove Task")
    print("4) Mark Task as done")
    print("5) Unmark Task")
    print("6) Exit")

#Check status and viewing tasks
def view_tasks():
    if not todo_list:
        print("\n NO task yet!!!  Add some :) ")
    else:
        print("\n Your Tasks: ")
        for i, task in enumerate(todo_list, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}.[{status}] {task['task']}")

#Adding task

def add_task():
    task = input("Enter your task: ")
    todo_list.append({"task": task , "done": False})
    print("Task Added!!!")

#Remove Task

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        removed = todo_list.pop(task_num -1)
        print(f"Removed task: {removed['task']}")
    except (IndexError , ValueError):
        print("INVALID  TASK NUMBER!!!")
 
 #Marking the task 
def mark_task():
    view_tasks()    
    try:
        task_num = int(input("Enter task number to mark as done: "))
        todo_list[task_num -1]["done"] = True
        print("Task marked as done!!! ")
    except (IndexError , ValueError):
        print("INVALID  TASK NUMBER!!!")

#Unmarking the task

def unmark_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to unmark : "))
        todo_list[task_num -1]["done"] = False
        print("Task unmarked !!! ")
    except (IndexError , ValueError):
        print("INVALID  TASK NUMBER!!!")
#main loop()

while True:
    show_menu()
    choice = input("\n Choose any option (1-6): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        mark_task()
    elif choice == '5':
        unmark_task()
    elif choice == '6':
        print("gOOd bYe!  ThankYOU!!!")
        break
    else:
        print("\n Invalid Choice, please try again! ")


#THE END
