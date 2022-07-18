#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 22:04:04 2022

@author: erik
"""
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

i = 0
max_id = str(0)

while True:
    with requests.session() as s:

        x = s.get("https://www.registeruz.sk/cruz-public/api/uctovne-jednotky?zmenene-od=2000-01-01&pravna-forma=101&pokracovat-za-id="+ max_id)
        id_ = x.json()['id']
        existujeDalsieId = x.json()['existujeDalsieId']
        
        print(id_)

        # for c in id_:
        #     r = "https://www.registeruz.sk/cruz-public/api/uctovna-jednotka?id="+str(c)
        #     print(r)


    
        # it = 0
        # for c in id_:
        #     it = it +1
        #     if it> 400:
        #         while it > 0:
        #             print("spim")
        #             time.sleep(60)
        #             print("probudil jsem se")
        #             it = 0
                
        #     m = s.get("https://www.registeruz.sk/cruz-public/api/uctovna-jednotka?id="+str(c))
        #     try:
        #         dic =m.json()["dic"]
        #     except KeyError:
        #         dic = None
    
        #     try:
        #         idUctovnychZavierok =m.json()["idUctovnychZavierok"]
        #     except KeyError:
        #         idUctovnychZavierok = None
                
    
            
        #     if 'stav' not in m.json():
        #         if 'datumZrusenia' not in m.json():    
                    
        #             try:
        #                     print(m.json()["ico"], dic, m.json()["skNace"], m.json()["nazovUJ"], m.json()["mesto"], m.json()["ulica"], m.json()["psc"], m.json()["datumZalozenia"], idUctovnychZavierok, m.json()["velkostOrganizacie"])
        #             except Exception as e:
        #                     print("err: ", c, e)
        #     else:
        #             print(m.json()["stav"], c)
        
        if existujeDalsieId:
            
            max_id = str(max(x.json()['id']))
        else:
            break
