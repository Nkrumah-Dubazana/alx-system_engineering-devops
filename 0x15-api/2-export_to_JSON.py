#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    username = user.get("username")
    todos = requests.get(url + "todos", params = {"userId": user_id}).json()

    with open("{}.json"format(user_id), "W") as jsonfile:
        json.dump({user_id: [{
            "tassk": t.get("title"),
            "completed": t.get("completed"),
            "username": username
         } for t in todos]}, jsonfile)
