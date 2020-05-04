#!/usr/bin/python3
import requests
from sys import argv
import csv
import os

if __name__ == "__main__":
    user_id = argv[1]
    file = open("{}.csv".format(user_id), "w")
    user_dict = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(user_id)).json()
    name = user_dict["name"]
    list_of_dict = requests.get('https://jsonplaceholder.\
typicode.com/users/{}/todos'.format(user_id)).json()
    rows = []
    for item in list_of_dict:
        user_id = item["userId"]
        completed = item["completed"]
        title = item["title"]
        row = [user_id, completed, title]
        rows.append(row)
    with file:
        writer = csv.writer(file)
        for item in rows:
            writer.writerow(item)
