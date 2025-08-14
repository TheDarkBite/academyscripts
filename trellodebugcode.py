import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

#trello stuff
API_KEY = os.getenv("TRELLO_API_KEY")
TOKEN = os.getenv("TRELLO_TOKEN")
LIST_ID = os.getenv("TRELLO_LIST_ID")

alreadyaddedcards = requests.get("https://api.trello.com/1/lists/" + LIST_ID + "/cards", headers={"Accept": "application/json"}, params={"key": API_KEY, "token": TOKEN}).json()

names = [record["name"] for record in alreadyaddedcards]

print(names)

create_response = requests.post(
    "https://api.trello.com/1/cards",
    headers={"Accept": "application/json"},
    params={
        "key": API_KEY,
        "token": TOKEN,
        "idList": LIST_ID,
        "name": "Dark",
        "desc": "test"
    }
)

create_response.raise_for_status()
card_id = create_response.json()['id']
print("Created card:", card_id)