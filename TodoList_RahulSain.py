tasks = []

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter a task to add: ")
        tasks.append(task)
        print(f"✅ Task added: '{task}'")

    elif choice == '2':
        if not tasks:
            print("📭 No tasks in the list.")
        else:
            print("\n📋 Your Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == '3':
        if not tasks:
            print("⚠️ No tasks to delete.")
        else:
            print("\n🗑️ Task Deletion")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"🗑️ Task removed: '{removed}'")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")

    elif choice == '4':
        print("👋 Exiting the To-Do List App. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please enter a number from 1 to 4.")
