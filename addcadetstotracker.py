import asyncio
import os
from dotenv import load_dotenv
from roblox import Client
import requests
import json

load_dotenv()

#trello stuff
API_KEY = os.getenv("TRELLO_API_KEY")
TOKEN = os.getenv("TRELLO_TOKEN")
LIST_ID = os.getenv("TRELLO_LIST_ID")
BOARD_ID = os.getenv("TRELLO_BOARD_ID")

ROBLOX_COOKIE = os.getenv("ROBLOX_COOKIE")

client = Client(ROBLOX_COOKIE)

async def get_members_by_rank(group_id: int, rank_name: str):
    group = await client.get_group(group_id)
    print(f"Searching for members with rank: {rank_name} in group: {group.name}")

    members = []
    async for member in group.get_members():
        if member.role.name.lower() == rank_name.lower():
            members.append([member.name, member.id])  # username

    return members

async def main():
    group_id = 2808300       # <- Replace with your group ID
    target_rank = "Applicant"  # <- Replace with your exact role name

    members = await get_members_by_rank(group_id, target_rank)

    if members:
        print(f"\nFound {len(members)} members with rank '{target_rank}':")
        alreadyaddedcards = requests.get("https://api.trello.com/1/boards/" + BOARD_ID + "/cards", headers={"Accept": "application/json"}, params={"key": API_KEY, "token": TOKEN}).json()
        alreadyaddednames = [alreadyaddedcard["name"] for alreadyaddedcard in alreadyaddedcards]
        for name in members:
            if name[0] in alreadyaddednames:
                continue            
            create_response = requests.post(
                "https://api.trello.com/1/cards",
                params={
                    "key": API_KEY,
                    "token": TOKEN,
                    "idList": LIST_ID,
                    "name": name[0],
                    "desc": name[1]
                }
            )
            create_response.raise_for_status()
            card_id = create_response.json()['id']
            print("Created card:", card_id)

if __name__ == "__main__":
    asyncio.run(main())
