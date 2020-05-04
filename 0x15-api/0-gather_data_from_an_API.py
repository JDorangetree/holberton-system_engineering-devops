#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user_dict = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(user_id)).json()
    list_of_dict = requests.get('https://jsonplaceholder.\
typicode.com/users/{}/todos'.format(user_id)).json()
    name = user_dict["name"]
    done = 0
    n_task = 0
    list_of_task = []
    for item in list_of_dict:
        if item["completed"] is True:
            done += 1
            list_of_task.append(item["title"])
        n_task += 1

    print('Employee {} is done with tasks({}/{})'.format(name, done, n_task))
    for i in list_of_task:
        print("\t {}".format(i))
