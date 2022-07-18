import time
import requests
import asyncio
from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor, as_completed
import datetime
import asyncio
import re
import time 
from timeit import default_timer
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from aiohttp import ClientSession
import aiohttp
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import MetaData, Table
from sqlalchemy import create_engine
from sqlalchemy.sql import table, column, select, insert, values


engine = create_engine('mysql://koheny:prase123@database-1.cko8gdllddky.us-east-1.rds.amazonaws.com:3306/koheny')



Base = automap_base()

m = list()

def parse(ico):
        
        s = requests.session()
        x = s.get('https://www.zrsr.sk/zr_ico.aspx')
        con = x.content
        soup = BeautifulSoup(con, 'html.parser')
        
        VIEWSTATE = soup.find("input", {"id": "__VIEWSTATE"})['value']
        EVENTVALIDATION = soup.find("input", {"id": "__EVENTVALIDATION"})['value']
        VIEWSTATEGENERATOR = soup.find("input", {"id": "__VIEWSTATEGENERATOR"})['value']
        code = x.status_code
        set_forms ={
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": VIEWSTATE,
            "__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR,
            "__EVENTVALIDATION": EVENTVALIDATION,
            "msg1": "IČO+musí+tvoriť+8+číslic!",
            "tico":	ico[0],
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
        ew = s.post('https://www.zrsr.sk/zr_vypis.aspx?ID=1&V=U', data=set_forms)
        cont = {
            "content": ew.content,
            "ico": ico[0],
            }
        return cont
        #for a in pr:
            #return str(a)+ "----" +str(ico[0])
                   # for d in a.find_all('dl'):
                   #    if d(text = "Prevádzkarne"):
                    #   return str(d)+ "----" +str(ico[0])
                   #        for k in d.find_all("dd"):
                    #           pass
                                  


        # with s.post('https://www.zrsr.sk/zr_vypis.aspx?ID=1&V=U', data=set_forms) as ew:
        #     if ew.status_code == 200:
        #         q = BeautifulSoup(ew.content, 'html.parser')
        #         pr = q.find_all('li')
        #         if pr is None:
        #             print("ne", ico)
        #         #print(q.find('dl').find_all('dd')[1])
        #         for a in pr:
        #             for d in a.find_all('dl'):
        #                 if d.find("span", {"class": "neaktivny"}) is None:
                            
        #                         if d.find("dt").get_text() in "Prevádzkarne":
        #                             pass
        
        #         # asyncio.run(async_main(pr))
        #         if pr is not None:
        #             if pr.find("span", {"class": "neaktivny"}) is None:
                        
        #                     print(pr.find_all("dt"), ico[0] )
        

    
Base = automap_base()

my_list = list()
Base.prepare(engine, reflect=True)
LoginData = Base.classes.blog_registeruz
db_session = Session(engine)
some_data = db_session.query(LoginData.ico).distinct()
db_session.close()
tasks = []
with ProcessPoolExecutor(max_workers=160) as executor:


    futures = [ executor.submit(parse, ico) for ico in some_data ]

    results = []
    for result in as_completed(futures):
        con = result.result()
        soup = BeautifulSoup(con["content"], 'html.parser')
        for a in soup.find_all('li'):
            
            for d in a.find_all('dl'):
                print(d)
                if d.find('dt').get_text() == "Prevádzkarne":
                    if d.find("span", {"class": "neaktivny"}) is None:
                        subject = a.find('p')
                        subject = subject.get_text().split("Deň vzniku oprávnenia")[0]
                        my_list.append({"ico": con["ico"],"subject":  subject.strip(), "provozovna": d.find("dd").get_text()})

                        
                        
                        
               
    
    
    start = datetime.datetime.now()
    print("start time:-", start)
    
    # ts store timestamp of current time
    end = datetime.datetime.now()
    print("current time:-", end)


async def async_db(ico_, provozovna_, predmet_):





    async with engine1.begin() as conn:
        


        
       pokemon = await conn.execute(
                insert(zrzr).values(ico=ico_, provozovna=provozovna_, predmet=predmet_)
            )
       return pokemon     
    await engine1.dispose()
        
async def main(my_list):

        tasks = []

        
        for p in my_list:

            tasks.append(asyncio.create_task(async_db(p["ico"], p["provozovna"], p["subject"])))
        
        original_pokemon = await asyncio.gather(*tasks)



metadata = MetaData(bind=engine)
zrzr = Table('zrsr', metadata, autoload=True)

engine1 = create_async_engine(
                        'mysql+aiomysql://koheny:prase123@database-1.cko8gdllddky.us-east-1.rds.amazonaws.com:3306/koheny', echo=True,
                    )
loop = asyncio.get_event_loop()
loop.run_until_complete(main(my_list))