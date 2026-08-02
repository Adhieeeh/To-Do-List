tasks = []

while True:
    print("\n----TO-DO LIST----")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        if tasks:
            print("\n--- Tasks ---")
            for i, t in enumerate(tasks, start=1):
                status = "✓" if t["done"] else "✗"
                print(f"{i}. [{status}] {t['task']}")
        else:
            print("No tasks available.")
    elif choice == '2':
        task = input("Enter the task: ")
        tasks.append({"task": task, "done": False})
    elif choice == '3':
        if tasks:
            print("\n--- Tasks ---")
            for i, t in enumerate(tasks, start=1):
                status = "✓" if t["done"] else "✗"
                print(f"{i}. [{status}] {t['task']}")
            try:
                task_index = int(input("Enter the task number to mark as completed: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks available.")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
    
    