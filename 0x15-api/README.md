# API

### **This directory contains 4 programs. The programs were written in Python programming language.**

## [0. Gather data from an API](https://github.com/ehabsmh/alx-system_engineering-devops/blob/main/0x15-api/0-gather_data_from_an_API.py)

- Using this [REST API](https://jsonplaceholder.typicode.com/), for a given employee ID, returns information about his/her TODO list progress.

- Accepts an integer as a parameter, which is the employee ID

---

## [1. Export to CSV](https://github.com/ehabsmh/alx-system_engineering-devops/blob/main/0x15-api/1-export_to_CSV.py)

- Exports the data that we got in [0. Gather data from an API](https://github.com/ehabsmh/alx-system_engineering-devops/blob/main/0x15-api/0-gather_data_from_an_API.py) in the CSV format ("USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE").

- File name must be: USER_ID.csv

---

## [2. Export to JSON](https://github.com/ehabsmh/alx-system_engineering-devops/blob/main/0x15-api/2-export_to_JSON.py)

- Exports the data that we got in [0. Gather data from an API](https://github.com/ehabsmh/alx-system_engineering-devops/blob/main/0x15-api/0-gather_data_from_an_API.py) in the JSON format

- Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}

- File name must be: USER_ID.json

---

## [3. Dictionary of list of dictionaries](https://github.com/ehabsmh/alx-system_engineering-devops/blob/main/0x15-api/3-dictionary_of_list_of_dictionaries.py)

- Exports the data that we got in [0. Gather data from an API](https://github.com/ehabsmh/alx-system_engineering-devops/blob/main/0x15-api/0-gather_data_from_an_API.py) in the JSON format

- Records all tasks from all employees
- Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}

- File name must be: todo_all_employees.json
