def todo_list():
    # Create empty list
    tasks = []

    # Loop until user quits 
    while True:
        print("\n📝 To-Do List Menu")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Quit")
        
        # Get user choice
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # --- Add Task ---
            task = input("Enter the task to add: ").strip()
            if task:
                tasks.append(task)
                print(f"'{task}' added to the list.")
            else:
                print("Task cannot be empty.")

        elif choice == '2':
            # --- View Tasks ---
            if tasks:
                print("\n📋 Your Current Tasks:")
                # Number the items when viewing
                for index, task in enumerate(tasks):
                    # Index starts at 0, so add 1 for user-friendly numbering
                    print(f"{index + 1}. {task}")
            else:
                print("\nThe list is empty! Go relax. 🏖️")

        elif choice == '3':
            # --- Remove Task ---
            if not tasks:
                print("\nNothing to remove, the list is empty.")
                continue
            
            # First, display the tasks with numbers so the user knows what to remove
            print("\n📋 Tasks to Remove:")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
                
            try:
                # Get the number of the task to remove
                task_number = int(input("Enter the number of the task to remove: "))
                
                # Check if the number is valid (within the list range)
                if 1 <= task_number <= len(tasks):
                    # List indices are 0-based, so subtract 1
                    removed_task = tasks.pop(task_number - 1)
                    print(f"✅ Removed task: '{removed_task}'")
                else:
                    print(f"Invalid number. Please enter a number between 1 and {len(tasks)}.")
                    
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        elif choice == '4':
            # --- Quit ---
            print("👋 Quitting application. Goodbye!")
            break  # Exit the while loop

        else:
            # Handle invalid menu choices
            print("❌ Invalid choice. Please enter a number between 1 and 4.")

# Test
# The function will run interactively until the user enters '4'
todo_list()

