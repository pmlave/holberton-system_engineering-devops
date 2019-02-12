#!/usr/bin/python3
import requests
import sys


def main():
    """main script function"""
    try:
        employee_id = sys.argv[1]
    except:
        return
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
            if thing.get('completed') is True:
                print("     {}".format(thing.get('title')))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
