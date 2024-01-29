#!/usr/bin/python3
"""This script returns information about his/her TODO list progress."""

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

        # Get completed todos made by specific employee ( by id)
        completed_todos = requests.get(todos_url, params={"completed": "true",
                                                        "userId": emp_id}).json()

        emp_name = emp.get("name")
        total_number_of_tasks = len(todos)
        number_of_done_tasks = len(completed_todos)

        print("Employee {} is done with tasks({}/{}):".format(
            emp_name,
            number_of_done_tasks,
            total_number_of_tasks
        ))

        for todo in completed_todos:
            print(f"\t {todo.get('title')}")
    
    except IndexError:
        print("Usage: ./0-gather_data_from_an_API.py EMP_ID")
    except Exception:
        print("Error while fetching data")
