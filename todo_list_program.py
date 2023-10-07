import os

class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = {"task": task, "completed": False}

    def complete_task(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]["completed"] = True

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]

    def show_tasks(self):
        if not self.tasks:
            print("Your To-Do List is empty.")
        else:
            print("To-Do List:")
            for task_id, task_info in self.tasks.items():
                status = "Completed" if task_info["completed"] else "Not Completed"
                print(f"{task_id}. {task_info['task']} - {status}")

    def save_tasks(self, filename):
        with open(filename, "w") as file:
            for task_id, task_info in self.tasks.items():
                file.write(f"{task_id},{task_info['task']},{task_info['completed']}\n")

    def load_tasks(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                for line in file:
                    task_id, task, completed = line.strip().split(",")
                    self.tasks[int(task_id)] = {"task": task, "completed": completed == "True"}

def main():
    todo_list = ToDoList()
    filename = "todo.txt"

    if os.path.exists(filename):
        todo_list.load_tasks(filename)

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. Show Tasks")
        print("5. Save Tasks")
        print("6. Quit")

        choice = input("Enter your task(choice): ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_id = int(input("Enter the task ID to mark as completed: "))
            todo_list.complete_task(task_id)
        elif choice == '3':
            task_id = int(input("Enter the task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == '4':
            todo_list.show_tasks()
        elif choice == '5':
            todo_list.save_tasks(filename)
            print("Tasks saved to 'todo.txt'.")
        elif choice == '6':
            print("Goodbye See You Again!")
            break
        else:
            print("Invalid choice. Please try again next time.")

if __name__ == "__main__":
    main()
