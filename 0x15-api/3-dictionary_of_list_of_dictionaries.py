#!/usr/bin/python3
"""This script returns information about his/her TODO list progress."""

import json
import requests

if __name__ == "__main__":
    try:
        # Get employee by ID
        users_url = "https://jsonplaceholder.typicode.com/users/"
        employees = requests.get(users_url).json()

        # Get all todos by specific employee (by id)
        todos_url = "https://jsonplaceholder.typicode.com/todos/"
        todos = requests.get(todos_url).json()

        emp_data = {}

        with open("todo_all_employees.json", "w") as wf:
            for emp in employees:
                emp_id = emp.get("id")
                emp_username = emp.get("username")

                # For each employee get the corresponding todos
                emp_data[emp_id] = [
                    {
                        "username": emp_username,
                        "task": todo.get("title"),
                        "completed": todo.get("completed"),
                    }
                    for todo in todos if todo.get("userId") == emp_id]

            json.dump(emp_data, wf)

    except Exception:
        print("Error while fetching data")
