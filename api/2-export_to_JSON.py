import requests
import sys
import json

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


    print(f"Employee{employee_name} is done with tasks({num_of_done_tasks}/{total_num_task}):")

    json_data = {
        id: [{
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name
            }
            for task in todo_data
        ]
    }

    with open(f'{id}.json', mode='w') as json_file:
        json.dump(json_data, json_file, indent=4)
