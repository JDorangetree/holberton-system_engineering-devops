#!/usr/bin/python3
import csv
import json
import os
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user_dict = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(user_id)).json()
    name = user_dict.get("username")
    list_of_dict = requests.get('https://jsonplaceholder.\
typicode.com/users/{}/todos'.format(user_id)).json()

    dict_to_json = {}
    list_todos = []
    for item in list_of_dict:
        my_dict = {}
        my_dict["task"] = item.get("title")
        my_dict["completed"] = item.get("completed")
        my_dict["username"] = name
        list_todos.append(my_dict)
    dict_to_json[user_id] = list_todos

    with open('{}.json'.format(user_id), 'w') as file:
        json.dump(dict_to_json, file)
