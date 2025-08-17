import asyncio
from roblox import Client
import os
from dotenv import load_dotenv
 
ROBLOX_COOKIE = os.getenv("ROBLOX_COOKIE")

client = Client(ROBLOX_COOKIE)


async def main():
    group = await client.get_group("758071")
    users = []
    for user in users:
