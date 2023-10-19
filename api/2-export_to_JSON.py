"""
    This module fetches employee information
    and their to-do list from a REST API and saves it in a JSON file.
"""
import json
import requests
import sys

# Function to fetch employee details
def fetch_employee_details(user_id):
    """
    Fetches employee details from the REST API.

    Args:
        user_id (int): The user ID for the employee.

    Returns:
        dict or None: A dictionary containing employee details or None if not found.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to fetch employee's TODO list
def fetch_employee_tasks(user_id):
    """
    Fetches a list of tasks owned by the employee from the REST API.

    Args:
        user_id (int): The user ID for the employee.

    Returns:
        list: A list of tasks in JSON format.
    """
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Function to calculate progress
def calculate_progress(tasks):
    """
    Calculates the progress of completed tasks.

    Args:
        tasks (list): A list of tasks.

    Returns:
        tuple: A tuple containing completed tasks and total tasks.
    """
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    return completed_tasks, total_tasks

# Function to display progress
def display_progress(username, completed_tasks, total_tasks):
    """
    Displays the progress of completed tasks for the employee.

    Args:
        username (str): The username of the employee.
        completed_tasks (int): The number of completed tasks.
        total_tasks (int): The total number of tasks.
    """
    print(f"Employee {username} is done with tasks({completed_tasks}/{total_tasks}):")

# Function to display completed task titles
def display_completed_tasks(tasks):
    """
    Displays the titles of completed tasks.

    Args:
        tasks (list): A list of tasks.
    """
    for task in tasks:
        if task['completed']:
            formatted_task_title = "\t {}".format(task['title'])
            print(formatted_task_title)

# Function to export data to a JSON file
def export_to_json(user_id, username, tasks):
    """
    Exports employee tasks to a JSON file.

    Args:
        user_id (int): The user ID for the employee.
        username (str): The username of the employee.
        tasks (list): A list of tasks.

    Outputs:
        Creates a JSON file with the employee's tasks.
    """
    data = {str(user_id): []}
    for task in tasks:
        data[str(user_id)].append({
            "task": task['title'],
            "completed": bool(task['completed']),
            "username": username
        })

    file_name = f"{user_id}.json"
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=2)

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: python modified_script.py <user_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    employee_details = fetch_employee_details(user_id)

    if employee_details is None:
        print(f"Employee with ID {user_id} not found.")
    else:
        username = employee_details['username']
        tasks = fetch_employee_tasks(user_id)
        completed_tasks, total_tasks = calculate_progress(tasks)
        display_progress(username, completed_tasks, total_tasks)
        display_completed_tasks(tasks)
        export_to_json(user_id, username, tasks)
        print(f"Tasks exported to {user_id}.json")
"""
