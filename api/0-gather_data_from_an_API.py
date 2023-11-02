#!/usr/bin/python3
import json
import requests
import sys

# Define the base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

def get_employee_todo_progress(employee_id):
    try:
        # Make a GET request to fetch the employee's TODO list
        response = requests.get(f"{BASE_URL}/todos?userId={employee_id}")

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            todos = json.loads(response.text)

            # Get the user's name
            user_response = requests.get(f"{BASE_URL}/users/{employee_id}")
            user_data = json.loads(user_response.text)
            employee_name = user_data["name"]

            # Calculate the number of completed and total tasks
            total_tasks = len(todos)
            completed_tasks = sum(1 for todo in todos if todo["completed"])

            # Display the progress information
            print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
            for todo in todos:
                if todo["completed"]:
                    print(f"\t{todo['title']}")

        else:
            print(f"Failed to fetch TODO list for employee ID {employee_id}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
