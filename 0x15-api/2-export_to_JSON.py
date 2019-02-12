#!/usr/bin/python3
"""Converting the data output to JSON format"""
import json
import requests
import sys


def main():
    """Main script function"""
    if len(sys.argv) == 1:
        """if no id given, set to empty string"""
        employee_id = ""
    else:
        employee_id = sys.argv[1]
    par = {'id': employee_id}
    emp = requests.get('https://jsonplaceholder.typicode.com/users',
                       params=par)
    emp = emp.json()

    par = {'userId': employee_id}
    todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                        params=par)
    todo = todo.json()
    jsonData = {}
    jsonList = []
    user = emp[0].get('username')
    for thing in todo:
        temp_dict = {"task": thing.get('title'),
                     "completed": thing.get('completed'),
                     "username": user}
        jsonList.append(temp_dict)
    jsonData[employee_id] = jsonList
    filename = employee_id + '.json'
    with open(filename, 'w') as jsonFile:
        json.dump(jsonData, jsonFile)

if __name__ == "__main__":
    main()
