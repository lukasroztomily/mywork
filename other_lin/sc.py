import datetime
import asyncio
from timeit import default_timer
from aiohttp import ClientSession
import aiohttp
import requests
from bs4 import BeautifulSoup
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.sql import table, column, select, insert, values


def fetch_async():


    loop = asyncio.get_event_loop() 
    future = asyncio.ensure_future(fetch_all())
    loop.run_until_complete(future) 




async def fetch_all():
    tasks = []
    fetch.start_time = dict() 
    Base = automap_base()

    engine = create_engine('mysql://koheny:prase123@database-1.cko8gdllddky.us-east-1.rds.amazonaws.com:3306/koheny')

    conn = engine.connect()
    Base.prepare(engine, reflect=True)
    LoginData = Base.classes.blog_registeruz
    db_session = Session(engine)
    some_data = db_session.query(LoginData.ico).distinct()
    async with ClientSession() as session:

        for icos in some_data:
            task = asyncio.ensure_future(fetch(icos[0], session))
            
            tasks.append(task) 
        _ = await asyncio.gather(*tasks) 

async def fetch(ico, session):
    
    async with session.get("https://www.zrsr.sk/zr_ico.aspx") as response:
        r = await response.read()
        s = requests.Session()
        con = r
        soup = BeautifulSoup(con, 'html.parser')
        
        VIEWSTATE = soup.find("input", {"id": "__VIEWSTATE"})['value']
        EVENTVALIDATION = soup.find("input", {"id": "__EVENTVALIDATION"})['value']
        VIEWSTATEGENERATOR = soup.find("input", {"id": "__VIEWSTATEGENERATOR"})['value']
        
        set_forms ={
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": VIEWSTATE,
            "__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR,
            "__EVENTVALIDATION": EVENTVALIDATION,
            "msg1": "IČO+musí+tvoriť+8+číslic!",
            "tico":	ico,
            "cmdVyhladat":"Vyhľadať"
            }
        content = s.post('https://www.zrsr.sk/zr_ico.aspx', data=set_forms)
        soup = BeautifulSoup(content.content, 'html.parser')
        
        VIEWSTATE = soup.find("input", {"id": "__VIEWSTATE"})['value']
        VIEWSTATEGENERATOR = soup.find("input", {"id": "__VIEWSTATEGENERATOR"})['value']
        
        set_forms ={
            "__VIEWSTATE": VIEWSTATE,
            "__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR
            }
        
        content = s.post('https://www.zrsr.sk/zr_vypis.aspx?ID=1&V=U', data=set_forms)
        soup = BeautifulSoup(content.content, 'html.parser')

        return soup


ct = datetime.datetime.now()
print("current time:-", ct)


fetch_async()


# ts store timestamp of current time
ct = datetime.datetime.now()
print("current time:-", ct)    
   