import csv
import requests
import sys

# Function to fetch tasks for a specific user
def fetch_tasks(user_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Function to export tasks to a CSV file
def export_to_csv(user_id, tasks):
    file_name = f"{user_id}.csv"
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for task in tasks:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": task['title'],
                "TASK_COMPLETED_STATUS": str(task['completed']),
                "TASK_TITLE": task['title']
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 1-export_to_CSV.py <user_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    tasks = fetch_tasks(user_id)
    if not tasks:
        print(f"No tasks found for user {user_id}")
    else:
        export_to_csv(user_id, tasks)
        print(f"Tasks exported to {user_id}.csv")

