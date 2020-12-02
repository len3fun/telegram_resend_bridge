import asyncio
from collections import namedtuple
import logging
import os

from telethon import TelegramClient, events


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
USER1_ID = os.getenv('USER1_ID')
USER2_ID = os.getenv('USER2_ID')
USER1_USERNAME = os.getenv('USER1_USERNAME')
USER2_USERNAME = os.getenv('USER2_USERNAME')


client = TelegramClient('anon', API_ID, API_HASH) 

User = namedtuple('User', 'name id username')
user1 = User('User1', USER1_ID, USER1_USERNAME)
user2 = User('User2', USER2_ID, USER2_USERNAME)


@client.on(events.NewMessage)
async def event_handler(event):
    sender = await event.get_sender()
    if sender.username == user2.username:
        try:
            await client.forward_messages(user1.id, event.message)
        except Exception as e:
            msg = "Bug report: User пытался отправить сообщение, но произошла ошибка."
            await client.send_message(user1.id, msg)


client.start()
client.run_until_disconnected()