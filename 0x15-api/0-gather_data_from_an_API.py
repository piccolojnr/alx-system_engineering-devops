#!/usr/bin/python3
"""_summary_
"""
import requests
from sys import argv

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = int(argv[1])
    todos_url = "{}/todos?userId={}".format(
        base_url,
        employee_id,
    )

    user_response = requests.get(
        base_url + "/users/{}".format(employee_id),
    )
    todos_response = requests.get(
        base_url + "/todos",
        params={"userId": employee_id},
    )

    user_data = user_response.json()
    todos_data = todos_response.json()

    completed_tasks = [task for task in todos_data if task["completed"]]
    total_tasks = len(todos_data)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user_data["name"], len(completed_tasks), total_tasks
        )
    )

    for task in completed_tasks:
        print("\t{}".format(task["title"]))
