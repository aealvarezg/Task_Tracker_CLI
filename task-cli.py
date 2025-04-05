import json
import os
from datetime import datetime
from argparse import ArgumentParser as arg
from tabulate import tabulate

# Path of the JSON file where the tasks will be saved
DATABASE_PATH = 'taskcli.json'

# Load tasks from JSON file (if exists)
def load_tasks():
    if os.path.exists(DATABASE_PATH):
        with open(DATABASE_PATH, 'r') as file:
            return json.load(file)
    return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(DATABASE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

# Generate a table with tabulate
def generate_table (data):
    return tabulate(data, ["Id", "Description", "Status", "Created At", "Updated At"], tablefmt="fancy_grid")

# Global list to store tasks (simulating a database)
tasks = load_tasks()

# Date format to HH:MM dd-mm-yy 
formated_time = datetime.now().strftime('%H:%M:%S %d/%m/%Y')

# Add a task
def add_task(args):
    last_id = max(task['id'] for task in tasks) if tasks else 0
    task = {'id': last_id + 1, 'description': args.name, 'status': 'todo', 'created_At': formated_time, 'updated_At': formated_time}
    tasks.append(task)
    save_tasks(tasks)
    print(generate_table([[task['id'], task['description'], task['status'], task['created_At'], task['updated_At']]]))

# Update a task
def update_task(args):
    task_id = args.id
    new_name = args.new_name
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_name
            task['updated_At'] = formated_time
            save_tasks(tasks)
            print(generate_table([[task['id'], task['description'], task['status'], task['created_At'], task['updated_At']]]))
            return
    print(f"No task found with Id = {task_id}")

# Delete a task
def delete_task(args):
    task_id = args.id
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(generate_table([[task['id'], task['description'], task['status'], task['created_At'], task['updated_At']]]))
            return 
    print(f"No task found with Id = {task_id}")                

# Mark a task as 'in-progress'
def mark_task_in_progress(args):
    task_id = args.id
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'in-progress'
            task['updated_At'] = formated_time
            save_tasks(tasks)
            print(generate_table([[task['id'], task['description'], task['status'], task['created_At'], task['updated_At']]]))
    print(f"No task found with Id = {task_id}")

# Mark a task as 'done'
def mark_task_done(args):
    task_id = args.id
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'done'
            task['updated_At'] = formated_time
            save_tasks(tasks)
            print(generate_table([[task['id'], task['description'], task['status'], task['created_At'], task['updated_At']]]))
            return
    print(f"No task found with Id = {task_id}")

# List tasks    
def list_tasks(args):
    status_filter = args.status
    filtered_tasks = tasks if status_filter is None else [task for task in tasks if task.get('status') == status_filter]

    if not filtered_tasks:
        print("There are not tasks to show")
    else:
        """ print("Tasks:")
        for task in filtered_tasks:
            print(f"Id: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['created_At']}, Updated At: {task['updated_At']}") """
        table_data = [[task['id'], task['description'], task['status'], task['created_At'], task['updated_At']] for task in filtered_tasks]
        print(generate_table(table_data))
            

def main():
    # Main parser
    parser = arg(description='A CLI app to track your tasks and manage your to-do list')
    subparsers = parser.add_subparsers(dest='command', help='Available subcommands')
    
    # 'add' subcommand
    add_parser = subparsers.add_parser('add', help='Add a new task to yor list')
    add_parser.add_argument('name', help='Task name')
    add_parser.set_defaults(func=add_task)

    # 'update' subcommand
    update_parser = subparsers.add_parser('update', help='Update an existing task')
    update_parser.add_argument('id', type=int, help='ID of the task to be updated')
    update_parser.add_argument('new_name', help='New task name')
    update_parser.set_defaults(func=update_task)

    # 'delete' subcommand
    delete_parser = subparsers.add_parser('delete', help='Delete a task from your list')
    delete_parser.add_argument('id', type=int, help='Enter the ID of the task you want to delete')
    delete_parser.set_defaults(func=delete_task)

    # 'mark-in-progress' subcommand
    mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark a taskas as in-progress')
    mark_in_progress_parser.add_argument('id', type=int, help='Enter the ID of the task you want to mark in-progress')
    mark_in_progress_parser.set_defaults(func=mark_task_in_progress)

    # 'mark-done' subcommand
    mark_done_parser = subparsers.add_parser('mark-done', help='Mark a taskas as done')
    mark_done_parser.add_argument('id', type=int, help='Enter the ID of the task you want to mark done')
    mark_done_parser.set_defaults(func=mark_task_done)

    # 'list' subcommand
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('-s', '--status', type=str, choices=['todo', 'in-progress', 'done'], help='Filter tasks by status')
    list_parser.set_defaults(func=list_tasks)

    # Parse the arguments and execute the corresponding function
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()