#!/usr/bin/python3
"""_summary_
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = int(argv[1])

    user_response = requests.get(base_url + "/users/{}".format(employee_id))
    todos_response = requests.get(base_url + "/todos", params={"userId": employee_id})

    user_data = user_response.json()
    todos_data = todos_response.json()

    completed_tasks = [
        task.get("title") for task in todos_data if task.get("completed") is True
    ]
    total_tasks = len(todos_data)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user_data.get("name"), len(completed_tasks), total_tasks
        )
    )

    for task in completed_tasks:
        print("\t{}".format(task))
