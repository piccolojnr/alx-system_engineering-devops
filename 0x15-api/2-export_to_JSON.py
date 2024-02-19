#!/usr/bin/python3
"""_summary_
"""
import requests
import json
from sys import argv


def export_to_json(user_id, username, tasks):
    """ """
    data = {"USER_ID": []}

    for task in tasks:
        data["USER_ID"].append(
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": username,
            }
        )

    filename = "{}.json".format("user_id")

    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id
    )

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()

        export_to_json(user_data["id"], user_data["username"], todos_data)

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
