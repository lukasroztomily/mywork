#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 17:17:38 2022

@author: erik
"""
import requests
import urllib.request as urllib2
import time
from urllib3.exceptions import ProtocolError
from requests.exceptions import ConnectionError, Timeout

files = open('api.txt', 'r')

fil = files.read().split('\n')
for i in fil:
    try:
        m = requests.get(i, timeout=180)
            
        try:
                dic =m.json()["dic"]
        except KeyError:
                dic = None
    
        try:
                idUctovnychZavierok =m.json()["idUctovnychZavierok"]
        except KeyError:
                idUctovnychZavierok = None
                
        if 'stav' not in m.json():
                if 'datumZrusenia' not in m.json():    
                    
                    try:
                            print(m.json()["ico"], dic, m.json()["skNace"], m.json()["nazovUJ"], m.json()["mesto"], m.json()["ulica"], m.json()["psc"], m.json()["datumZalozenia"], idUctovnychZavierok, m.json()["velkostOrganizacie"], )
                    except Exception as e:
                            print("err: ", e, m.json()["ico"], m.json()["id"])
        else:
                    print(m.json()["stav"], i)
        
    except (ProtocolError, ConnectionError, Timeout):
        print("Problem")
        time.sleep(60)
        print("Zkusim")
        m = requests.get(i)
        print("ok")
        try:
                dic =m.json()["dic"]
        except KeyError:
                dic = None
                
        try:
                ulica =m.json()["ulica"]
        except KeyError:
                ulica = None
    
        try:
                idUctovnychZavierok =m.json()["idUctovnychZavierok"]
        except KeyError:
                idUctovnychZavierok = None
                
        if 'stav' not in m.json():
                if 'datumZrusenia' not in m.json():    
                    
                    try:
                            print(m.json()["ico"], dic, m.json()["skNace"], m.json()["nazovUJ"], m.json()["mesto"], ulica, m.json()["psc"], m.json()["datumZalozenia"], idUctovnychZavierok, m.json()["velkostOrganizacie"])
                    except Exception as e:
                            print("err: ", e, m.json()["ico"])
        else:
                    print(m.json()["stav"], i)
        
        
    
    
files.close()



#     m = requests.get("https://www.registeruz.sk/cruz-public/api/uctovna-jednotka?id="+str(c))
        #     try:
        #         dic =m.json()["dic"]
        #     except KeyError:
        #         dic = None
    
        #     try:
        #         idUctovnychZavierok =m.json()["idUctovnychZavierok"]
        #     except KeyError:
        #         idUctovnychZavierok = None