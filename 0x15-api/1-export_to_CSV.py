#!/usr/bin/python3
"""_summary_
"""
import requests
import csv
from sys import argv


def export_to_csv(user_id, user_name, tasks):
    """ """
    filename = "{}.csv".format(user_id)

    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for task in tasks:
            writer.writerow(
                {
                    "USER_ID": user_id,
                    "USERNAME": user_name,
                    "TASK_COMPLETED_STATUS": str(task["completed"]),
                    "TASK_TITLE": task["title"],
                }
            )


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

        export_to_csv(user_data["id"], user_data["username"], todos_data)

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
