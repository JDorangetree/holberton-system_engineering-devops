#!/usr/bin/python3
import requests
from sys import argv
import csv
import os

if __name__ == "__main__":
    user_id = argv[1]
    user_dict = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(user_id)).json()
    name = user_dict["username"]
    list_of_dict = requests.get('https://jsonplaceholder.\
typicode.com/users/{}/todos'.format(user_id)).json()
    rows = []
    for item in list_of_dict:
        user_id = str(item["userId"])
        completed = str(item["completed"])
        title = item["title"]
        row = [user_id, name, completed, title]
        rows.append(row)
    with open("{}.csv".format(user_id), "w") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
        spamwriter.writerows(rows)
