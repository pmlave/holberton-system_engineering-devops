#!/usr/bin/python3
import requests
import sys


def main():
    """main script function"""
    if len(sys.argv) == 1:
        """if no id given, set to empty string"""
        employee_id = ""
    else:
        employee_id = sys.argv[1]
    try:
        par = {'id': employee_id}
        emp = requests.get('https://jsonplaceholder.typicode.com/users',
                           params=par)
        emp = emp.json()

        par = {'userId': employee_id}
        todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                            params=par)
        todo = todo.json()
        total = 0
        finished = 0
        for thing in todo:
            if thing.get('completed') is True:
                finished += 1
            total += 1
        print("Employee {} is done with tasks({:d}/{:d}):".format(
            emp[0].get('name'), finished, total))
        for thing in todo:
            if thing.get('completed') is False:
                print("     {}".format(thing.get('title')))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
