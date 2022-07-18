import asyncio
from timeit import default_timer
from aiohttp import ClientSession
import aiohttp
import requests
from bs4 import BeautifulSoup

# def fetch_async(urls):
#     start_time = default_timer()

#     loop = asyncio.get_event_loop() 
#     future = asyncio.ensure_future(fetch_all(urls))
#     loop.run_until_complete(future) 

#     tot_elapsed = default_timer() - start_time
#     print('Total time taken : ',  str(tot_elapsed))

# async def fetch_all(urls):
#     tasks = []
#     fetch.start_time = dict() 
#     async with ClientSession() as session:

#         for url in urls:
#             task = asyncio.ensure_future(fetch(url, session))

#             tasks.append(task) 
#         _ = await asyncio.gather(*tasks) 

# async def fetch(url, session):
#     fetch.start_time[url] = default_timer()
#     async with session.get(url) as response:
#         r = await response.read()
#         elapsed = default_timer() - fetch.start_time[url]
#         print(url ,  ' took ' ,  str(elapsed))
#         return r



# if __name__ == '__main__':
#     urls = ['https://nytimes.com',
#                 'https://github.com',
#                 'https://google.com',
#                 'https://reddit.com',
#                 'https://producthunt.com']
#     fetch_async(urls)
    
    
import time

start_time = time.time()


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon['name']


async def main():

   async with aiohttp.ClientSession() as session:

        tasks = []
        for number in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))





# async def get_data_url(session):


#     async with session.get(url='https://www.zrsr.sk/zr_ico.aspx') as response:
#         response.raise_for_status()
#         con =  await response.read()
#         soup = BeautifulSoup(con, 'html.parser')
        
#         VIEWSTATE = soup.find("input", {"id": "__VIEWSTATE"})['value']
#         EVENTVALIDATION = soup.find("input", {"id": "__EVENTVALIDATION"})['value']
#         VIEWSTATEGENERATOR = soup.find("input", {"id": "__VIEWSTATEGENERATOR"})['value']
#         set_forms ={
#             "__EVENTTARGET": "",
#             "__EVENTARGUMENT": "",
#             "__VIEWSTATE": VIEWSTATE,
#             "__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR,
#             "__EVENTVALIDATION": EVENTVALIDATION,
#             "msg1": "IČO+musí+tvoriť+8+číslic!",
#             "tico":"36813818",
#             "cmdVyhladat":"Vyhľadať"
#             }
        
#         async with session.post(url="https://www.zrsr.sk/zr_browse.aspx", data= set_forms) as response:
#                 response.raise_for_status()
#                 con =   await response.read()
#                 print(con)
#                 soup =  BeautifulSoup(con, 'html.parser')
                
#                 VIEWSTATE =  soup.find("input", {"id": "__VIEWSTATE"})['value']
#                 VIEWSTATEGENERATOR =  soup.find("input", {"id": "__VIEWSTATEGENERATOR"})['value']
                
#                 set_forms ={
#                     "__VIEWSTATE": VIEWSTATE,
#                     "__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR
#                     }       

        

#     async with session.post(url="https://www.zrsr.sk/zr_vypis.aspx?ID=1&V=U",  data= set_forms) as status_response:
#             status_response.raise_for_status()
#             con =  await status_response.read()
            
#             if status_response.status == 201:
#                 return con
#         # await asyncio.sleep(10)

# async def main():
    
#     async with aiohttp.ClientSession() as session:
#         data_url = await get_data_url(session)
#         return data_url
# asyncio.run(main())