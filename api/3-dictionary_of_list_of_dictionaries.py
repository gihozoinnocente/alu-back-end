#!/usr/bin/python3
"""Exports data in the JSON format"""

import json
import requests

if __name__ == "__main":
    # Fetch user and task data from the JSONPlaceholder API
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')

    if users_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to fetch data from the API.")
        exit(1)

    users = users_response.json()
    todos = todos_response.json()

    # Create a dictionary to store tasks for all employees
    todo_all_employees = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        # Filter tasks for the current user
        user_tasks = [{"username": username, "task": task['title'], "completed": task['completed']}
                     for task in todos if task['userId'] == user_id]

        # Add the tasks to the dictionary
        todo_all_employees[user_id] = user_tasks

    # Write the data to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(todo_all_employees, json_file, indent=4)

    print("Data exported to todo_all_employees.json")
