#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 15:58:46 2022

@author: erik
"""

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.sql import table, column, select, insert, values

Base = automap_base()

engine = create_engine('mysql://koheny:prase123@database-1.cko8gdllddky.us-east-1.rds.amazonaws.com:3306/koheny')

conn = engine.connect()

with conn as c:
    t = table('accounts_account')
    s = select('*', t)

    Base.prepare(engine, reflect=True)
    
    # mapped classes are now created with names by default
    # matching that of the table name.
    
    

    comp = s.compile(compile_kwargs={"literal_binds": True})
    t = c.execute(comp)
    
    LoginData = Base.classes.blog_registeruz
    #stmt = (insert(LoginData).values(ico='username', nazovUJ='Full asdas'))
    #c.execute(stmt)

        

Base.prepare(engine, reflect=True)
LoginData = Base.classes.blog_registeruz
db_session = Session(engine)
some_data = db_session.query(LoginData.ico).distinct()

for a in some_data:
    print(a[0])
