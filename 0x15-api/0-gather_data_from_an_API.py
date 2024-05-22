#!/usr/bin/python3
"""
Module 0-gather_data_from_an_API:

Using 'https://jsonplaceholder.typicode.com', for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        SRC = 'https://jsonplaceholder.typicode.com/'
        id = int(argv[1])
        res_user = requests.get('{}users/{}'.format(SRC, id)).json()
        res_todos = requests.get('{}todos?userId={}'.format(SRC, id)).json()
        name = res_user.get('name')
        todos = list(res_todos)
        todos_done = list(filter(lambda x: x.get('completed'), todos))
        print(
            'Employee {} is done with tasks({}/{}):'.format(
                name,
                len(todos_done),
                len(todos))
        )
        for todo_done in todos_done:
            print('\t {}'.format(todo_done.get('title')))
