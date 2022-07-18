import random
import requests
import re
from bs4 import BeautifulSoup

s = requests.Session()

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
    "tico":	"",
    "cmdVyhladat":"Vyhľadať"
    }

content = s.post('https://www.zrsr.sk/zr_ico.aspx', data=set_forms)
soup = BeautifulSoup(content.content, 'html.parser')

VIEWSTATE = soup.find("input", {"id": "__VIEWSTATE"})['value']
EVENTVALIDATION = soup.find("input", {"id": "__EVENTVALIDATION"})['value']
VIEWSTATEGENERATOR = soup.find("input", {"id": "__VIEWSTATEGENERATOR"})['value']

set_forms ={
    "__EVENTTARGET": "DataGrid1$ctl14$ctl01",
    "__EVENTARGUMENT": "",
    "__VIEWSTATE": VIEWSTATE,
    "__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR,
    "__EVENTVALIDATION": EVENTVALIDATION
    }

c = None
content = s.post('https://www.zrsr.sk/zr_browse.aspx', data=set_forms)

while True:
    soup = BeautifulSoup(content.content, 'html.parser')
    a = soup.find('td', {'colspan': '5'})
    
    
    next_site = a.prettify().split('</span>')[1]
    soups= BeautifulSoup(next_site, 'html.parser') 

    
    

    
    if len(soups.find_all("a")) > 0:
        x = re.search("\('([^']+)",str(soups.find("a")['href']))  
        EVENTTARGET = x.group(1)
        
        VIEWSTATE = soup.find("input", {"id": "__VIEWSTATE"})['value']
        EVENTVALIDATION = soup.find("input", {"id": "__EVENTVALIDATION"})['value']
        VIEWSTATEGENERATOR = soup.find("input", {"id": "__VIEWSTATEGENERATOR"})['value']
        
        set_forms ={
            "__EVENTTARGET": EVENTTARGET,
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": VIEWSTATE,
            "__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR,
            "__EVENTVALIDATION": EVENTVALIDATION
            }
        
        content = s.post('https://www.zrsr.sk/zr_browse.aspx', data=set_forms)
        
    else:
        print(a)
        break
