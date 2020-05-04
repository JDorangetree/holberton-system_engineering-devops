#!/usr/bin/python3
import json
import os
import requests

if __name__ == "__main__":
    index = 1
    dict_to_json = {}
    while index < 11:
        user_dict = requests.get('https://jsonplaceholder.typicode.\
com/users/{}'.format(index)).json()
        name = user_dict.get("username")
        list_of_dict = requests.get('https://jsonplaceholder.\
typicode.com/users/{}/todos'.format(index)).json()
        list_for_id = []
        for item in list_of_dict:
            my_dict = {}
            my_dict["task"] = item.get("title")
            my_dict["completed"] = item.get("completed")
            my_dict["username"] = name
            list_for_id.append(my_dict)
        dict_to_json[index] = list_for_id
        index += 1
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dict_to_json, file)
