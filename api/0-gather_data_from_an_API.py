#!/usr/bin/python3
import requests
import sys

# Function to get TODO list progress for a given employee ID
def get_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()

        # Fetch TODO list for the user
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Calculate the progress
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for task in todos_data if task["completed"])

        # Display progress information
        print(f"Employee {user_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")
        print(f"EMPLOYEE_NAME: {user_data['name']}")
        print(f"NUMBER_OF_DONE_TASKS: {completed_tasks}")
        print(f"TOTAL_NUMBER_OF_TASKS: {total_tasks}")

        # Display completed task titles
        print("Completed Tasks:")
        for task in todos_data:
            if task["completed"]:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python todo_progress.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_progress(employee_id)

