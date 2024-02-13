#!/usr/bin/python3
"""This script returns information about his/her TODO list progress."""

import json
import requests
from sys import argv

if __name__ == "__main__":
    try:
        emp_id = argv[1]

        # Get employee by ID
        users_url = "https://jsonplaceholder.typicode.com/users/{}"
        emp = requests.get(users_url.format(emp_id)).json()

        # Get all todos by specific employee (by id)
        todos_url = "https://jsonplaceholder.typicode.com/todos/"

        todos = requests.get(todos_url, params="userId={}".
                             format(emp_id)).json()

        emp_username = emp.get("username")

        # Data formatting to be written to a json file
        emp_format = {
            emp_id: [
                {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": emp_username
                }
                for todo in todos]
        }

        # Inserting the data to the json file
        with open(f"{emp_id}.json", "w") as wf:
            json.dump(emp_format, wf)

    except IndexError:
        print("Usage: ./2-export_to_JSON.py EMP_ID")
    except Exception:
        print("Error while fetching data")
