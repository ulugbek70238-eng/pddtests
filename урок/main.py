import asyncio
import aiohttp
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            web_content = await response.text()
            soup = BeautifulSoup(web_content, 'html.parser')
            quotes = soup.find_all('span', {'class', 'text'})

            for i in quotes:
                print(i.string)

asyncio.run(main())