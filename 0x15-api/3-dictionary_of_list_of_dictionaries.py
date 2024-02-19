#!/usr/bin/python3
"""_summary_
"""
import requests
import json


def export_to_json(data):
    """ """
    filename = "todo_all_employees.json"

    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)

    print("JSON file '{}' created successfully.".format(filename))


def fetch_tasks():
    all_tasks = {}

    for user_id in range(1, 11):  # Assuming user IDs are from 1 to 10
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
        todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            user_id
        )

        try:
            user_response = requests.get(user_url)
            todos_response = requests.get(todos_url)

            user_data = user_response.json()
            todos_data = todos_response.json()

            all_tasks[user_id] = []

            for task in todos_data:
                all_tasks[user_id].append(
                    {
                        "username": user_data["username"],
                        "task": task["title"],
                        "completed": task["completed"],
                    }
                )

        except requests.exceptions.RequestException as e:
            print("Error fetching data for user {}: {}".format(user_id, e))

    return all_tasks


if __name__ == "__main__":
    all_tasks_data = fetch_tasks()
    export_to_json(all_tasks_data)
