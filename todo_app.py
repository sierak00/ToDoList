import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"✔ Task '{tasks[index]['task']}' marked as done!")
    else:
        print("❌ Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑 Deleted task: {removed['task']}")
    else:
        print("❌ Invalid task number.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    print("\n📝 Your Tasks:")
    for i, t in enumerate(tasks):
        status = "✅" if t["done"] else "⏳"
        print(f"{i}. {t['task']} {status}")
    print()

def main():
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_task(input("Enter task: "))
        elif choice == "2":
            mark_done(int(input("Enter task number to mark done: ")))
        elif choice == "3":
            delete_task(int(input("Enter task number to delete: ")))
        elif choice == "4":
            list_tasks()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option, try again.")

if __name__ == "__main__":
    main()
