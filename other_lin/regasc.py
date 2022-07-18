#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 22:00:11 2022

@author: erik
"""
import urllib3
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
from aiohttp import ClientSession, ClientTimeout
import aiohttp
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import MetaData, Table
from sqlalchemy import create_engine
from sqlalchemy.sql import table, column, select, insert, values


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        print(pokemon)
        return pokemon


async def main(in_):
   tasks = []
   c = []
   i = 0
   max_id = str(0)
   timeout = ClientTimeout(total=600)
   async with aiohttp.ClientSession() as session:
     
            for i in in_:


                url = "https://www.registeruz.sk/cruz-public/api/uctovna-jednotka?id="+ str(i)
                tasks.append(asyncio.ensure_future(get_pokemon(session, url)))
        
            original_pokemon = await asyncio.gather(*tasks)
            for pokemon in original_pokemon:
                if 'stav' not in pokemon:
                    if 'datumZrusenia' not in pokemon:

                        try:
                          idUctovnychZavierok =pokemon["idUctovnychZavierok"]
                        except KeyError:
                          idUctovnychZavierok = None
                        
         
                        try:
                          dic = pokemon["dic"]
                        except KeyError:
                          dic = None
                          
                        try:
                          ulica = pokemon["ulica"]
                        except KeyError:
                          ulica = None
                          
                        try:
                          mesto = pokemon["mesto"]
                        except KeyError:
                          mesto = None
                          
                        try:
                          psc = pokemon["psc"]
                        except KeyError:
                          psc = None
                        
                        c.append({'ico': pokemon['ico'], 'nazovUJ': pokemon['nazovUJ'], 'idUctovnychZavierok': idUctovnychZavierok })
            return c

def reg():
    ids= []
    i = 0
    max_id = str(0)    
    while True:
        with requests.session() as s:
            try:
                x = s.get("https://www.registeruz.sk/cruz-public/api/uctovne-jednotky?zmenene-od=2000-01-01&pravna-forma=101&pokracovat-za-id="+ max_id)
            except (requests.exceptions.ConnectionError, urllib3.exceptions.ProtocolError):
                x = s.get("https://www.registeruz.sk/cruz-public/api/uctovne-jednotky?zmenene-od=2000-01-01&pravna-forma=101&pokracovat-za-id="+ max_id)
            
            id_ = x.json()['id']
            existujeDalsieId = x.json()['existujeDalsieId']
            
            m = asyncio.run(main(id_))
    
            if existujeDalsieId:
                
                max_id = str(max(x.json()['id']))
            else:
                break
    return m

a = reg()

            




async def async_db_class(ico_, nazovUJ, ucet = []):





    async with engine1.begin() as conn:
        


        
       pokemon = await conn.execute(
                insert(zrzr).values(ico=ico_, nazovUJ=nazovUJ)
            )
       
       if ucet is not None:
          for w in ucet:
               pokemon = await conn.execute(
                    insert(ucetzaverka).values(ico=ico_, ucet=w)
                )
    await engine1.dispose()
    

async def main_db(my_list):

        tasks = []

        
        for p in my_list:
            
            tasks.append(asyncio.ensure_future(async_db_class(p["ico"], p["nazovUJ"], p["idUctovnychZavierok"]    )))

        original_pokemon = await asyncio.gather(*tasks)


engine = create_engine('mysql://koheny:prase123@database-1.cko8gdllddky.us-east-1.rds.amazonaws.com:3306/koheny')
metadata = MetaData(bind=engine)
zrzr = Table('registeruz', metadata, autoload=True)
ucetzaverka = Table('ucetzaverka', metadata, autoload=True)

engine1 = create_async_engine(
                        'mysql+aiomysql://koheny:prase123@database-1.cko8gdllddky.us-east-1.rds.amazonaws.com:3306/koheny', echo=True,
                    )
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main_db(a))