import datetime

def add_task():
    task_name = input("Enter the task name: ")
    year, month, day = map(int, input("Enter the due date in yyyy-mm-dd format: ").split("-"))
    hour, minute = map(int, input("Enter the due time in hh:mm format: ").split(":"))
    due_date = datetime.datetime(year, month, day, hour, minute)
    return {"name": task_name, "due_date": due_date}

def main():
    tasks = []
    while True:
        print("Select an option:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = add_task()
            tasks.append(task)
            print("Task added!")
        elif choice == "2":
            now = datetime.datetime.now()
            for task in tasks:
                if task["due_date"] > now:
                    print(task["name"], task["due_date"].strftime("%Y-%m-%d %H:%M"))
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
