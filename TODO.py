import os

Tasks = []

def add():
    newtask = input("Enter the task: ")
    Tasks.append("[ ]" + newtask + '\n')
    with open("Tasks.txt", "a") as file:
        file.write("[ ]" + newtask + '\n')

def finish():
    k = int(input("Which index do you finish: "))
    with open("Tasks.txt", "r") as file:
        content = file.readlines()
    content[k] = "[X]" + content[k][3:]

    with open("Tasks.txt", "w") as file:
        file.writelines(content)

def display():
    with open("Tasks.txt", "r") as file:
        for line in file:
            print(line.strip())

def delete():
    with open("Tasks.txt", "r") as file:
        removed = file.readlines()

    delline = int(input('Enter the line you want to delete: '))
    del removed[delline]
    with open("Tasks.txt", 'w') as file:
        file.writelines(removed)

def clear():
    open("Tasks.txt", "w").close()

def main():
    while True:
        choice = input("[1: for add task] \n[2: to mark finish task] \n[3: to display tasks] \n[4: delete task] \n[5: delete all]\n[6: exit]\n: ")
        if choice == "1":
            add()
        elif choice == "2":
            finish()
        elif choice == "3":
            display()
        elif choice == "4":
            delete()
        elif choice == "5":
            clear()
        elif choice == "6":
            break
        else:
            print("Not in choices")
        input("Press Enter to continue...")  # Pause before next iteration

if __name__ == "__main__":
    main()
