#!/usr/bin/python3
"""This script returns information about his/her TODO list progress."""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    try:
        emp_id = argv[1]

        # Get employee by ID
        emp = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(
            emp_id)
        ).json()

        # Get all todos by specific employee (by id)
        todos_url = "https://jsonplaceholder.typicode.com/todos/"

        todos = requests.get(todos_url, params="userId={}".format(emp_id)
                            ).json()

        emp_username = emp.get("username")

        # Export data in the CSV format.
        with open(f"{emp_id}.csv", "w") as wf:
            csv_writer = csv.writer(wf, quotechar='"', quoting=csv.QUOTE_ALL)

            for todo in todos:
                csv_writer.writerow([emp_id, emp_username,
                                    todo.get("completed"),
                                    todo.get("title")])
    except IndexError:
        print("Usage: ./1-export_to_CSV.py EMP_ID")
    except Exception:
        print("Error while fetching data")
