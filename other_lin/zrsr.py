#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time


import datetime



from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.sql import table, column, select, insert, values,distinct

def zrsr():
    engine = create_engine('mysql://koheny:prase123@database-1.cko8gdllddky.us-east-1.rds.amazonaws.com:3306/koheny')
    conn = engine.connect()
    Base = automap_base()
    
    
    s = requests.Session()
    Base.prepare(engine, reflect=True)
    db_session = Session(engine)
    LoginData = Base.classes.blog_registeruz
    some_data = db_session.query(LoginData.ico).distinct()
    
    for c in some_data:
    
        x = s.get('https://www.zrsr.sk/zr_ico.aspx')
        con = x.content
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
            "tico":	c[0],
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



ct = datetime.datetime.now()
print("current time:-", ct)
zrsr()
# ts store timestamp of current time
ct = datetime.datetime.now()
print("current time:-", ct)

#https://metais.vicepremier.gov.sk/codelistrepository/codelists/codelistheaders/CL000025/codelistitems?language=sk&pageNumber=1&perPage=3000&effective=true&ascending=true    
#a = requests.get('https://metais.vicepremier.gov.sk/codelistrepository/codelists/codelistheaders/CL005205/codelistitems?language=sk&pageNumber=1&perPage=900&effective=true&ascending=true')

# print(a.json()['codelistsItems'][0]['itemCode'])