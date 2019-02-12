#!/usr/bin/python3
"""Exports the output of our API call to CSV format"""
import csv
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
        csv.register_dialect('myDialect',
                             quoting=csv.QUOTE_ALL,
                             skipinitialspace=True)

        csvData = []
        username = emp[0].get('username')
        for thing in todo:
            csvData.append([employee_id,
                            username,
                            thing.get('completed'),
                            thing.get('title')])

        file = employee_id + '.csv'
        with open(file, 'w') as csvFile:
            written = csv.writer(csvFile, dialect='myDialect')
            written.writerows(csvData)
        csvFile.close()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
