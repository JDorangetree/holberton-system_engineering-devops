#!/usr/bin/python3
import csv
import os
import requests
from sys import argv

if __name__ == "__main__":
    try:
        user_id = int(argv[1])
    except ValueError:
        exit()
    if int(user_id) > 10:
        exit()
    user_dict = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(user_id)).json()
    name = user_dict.get("username")
    list_of_dict = requests.get('https://jsonplaceholder.\
typicode.com/users/{}/todos'.format(user_id)).json()
    rows = []
    for item in list_of_dict:
        user_id = item.get("userId")
        completed = item.get("completed")
        title = item.get("title")
        row = [user_id, name, completed, title]
        rows.append(row)
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
        spamwriter.writerows(rows)
