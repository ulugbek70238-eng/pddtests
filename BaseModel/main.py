import asyncio
from asyncio import sleep

async def message(users):
    for i in users:
        print(i)

user_list = ['jordan', 'mike', 'nike']



asyncio.run(message(user_list))
print('Hello World')