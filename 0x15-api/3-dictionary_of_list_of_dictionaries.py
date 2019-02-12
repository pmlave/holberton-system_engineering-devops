#!/usr/bin/python3
"""Converting the data output to JSON format"""
import json
import requests
import sys


def main():
    """Main script function"""
    emp = requests.get('https://jsonplaceholder.typicode.com/users')
    emp = emp.json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo = todo.json()

    jsonData = {}
    for each_user in emp:
        employee_id = each_user.get('id')
        user = each_user.get('username')
        userData = {}
        jsonList = []
        for thing in todo:
            if thing.get('userId') == employee_id:
                temp_dict = {}
                temp_dict = {"task": thing.get('title'),
                             "completed": thing.get('completed'),
                             "username": user}
                jsonList.append(temp_dict)
        jsonData[employee_id] = jsonList

    with open('todo_all_employees.json', 'w') as jsonFile:
        json.dump(jsonData, jsonFile)

if __name__ == "__main__":
    main()
