#!/usr/bin/python3
import requests
import sys


def main():
    """main script function"""
    try:
        employee_id = sys.argv[1]
    except:
        return
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
    complete = []
    for thing in todo:
        if thing.get('completed') is True:
            finished += 1
            complete.append(thing.get('title'))
        total += 1
    print("Employee {} is done with tasks({}/{}):".format(
        emp[0].get('name'), finished, total))
    for thing in complete:
        print("\t {}".format(thing))

if __name__ == "__main__":
    main()
