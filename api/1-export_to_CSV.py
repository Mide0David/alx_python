import requests
import sys
import csv

if __name__ == '__main__':

    id = sys.argv[1]
    todo = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    employee = f"https://jsonplaceholder.typicode.com/users/{id}"

    #employee name
    response = requests.get(employee)
    data = response.json()
    employee_name = data['name']

    #todo list
    todo_result = requests.get(todo)
    todo_data = todo_result.json()
    num_of_done_tasks = sum(1 for task in todo_data if task['completed'] )
    total_num_task = len(todo_data)

    csv_file = "USER_ID.csv"

    with open(f'{id}.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        
        for task in todo_data:
            csv_writer.writerow([id, employee_name, task['completed']])

    print(f"Data has been exported to {csv_file}")
