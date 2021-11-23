
import aiohttp
import asyncio
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

async def get_page(session, url):
    async with session.get(url) as r:
        return await r.text()

async def get_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(get_page(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results

async def main(urls):
    async with aiohttp.ClientSession() as session:
        data = await get_all(session, urls)
        return data

def parse(results):
    title = []
    price = []
    for html in results:

        soap = BeautifulSoup(html, "html.parser" )
        title_ = soap.find_all('div', class_ = 'image_container')
        price_ = soap.find_all('p', class_ = 'price_color')
        
        for x in price_:
            x = x.text.strip()
            x = x.replace('£', '')
            price.append(float  (x))

        for x in title_:
            title_element = x.find("a")
            
            for x in title_element.find_all("img", alt=True):
                title.append(x['alt'])

    datarow = {'title':title, 'price':price}
    df = pd.DataFrame(data=datarow)
    df = df.sort_values(by=['price'], ascending=False)
    print(df)
    

def link():
    url =  'https://books.toscrape.com/catalogue/page-1.html'
    urls = []
    page = requests.get(url)
    soap = BeautifulSoup(page.content, "html.parser" )
    soapfind = soap.find('li', class_ ='current')
    txt = soapfind.text.strip()
    pagesize = re.findall("\d+", txt)[1]
    for i in range(1, int(pagesize)+1):
        x = 'https://books.toscrape.com/catalogue/page-%i.html'% (i)
        urls.append(x)
    return urls



x = link()
result = asyncio.run(main(x))

parse(result)

