# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import json
from sqlalchemy import create_engine
from sqlalchemy.sql import table, column, select, insert, values


class RegPipeline:

        
        
    # def process_item(self, item, spider):
    #     Base = automap_base()
    #     Base.prepare(self.engine, reflect=True)
    #     db_session = Session(self.engine)
        
    #     registeruz = Base.classes.blog_registeruz
    #     registeruzstmt = (insert(registeruz).values(ico=item["ico"], nazovUJ=item["nazovUJ"]))
    #     self.conn.execute(registeruzstmt)
    #     try:
    #         ucetnizaverka_ = Base.classes.blog_ucetnizaverka
    #         if item["idUctovnychZavierok"] is not None:
    #             for a in item["idUctovnychZavierok"]:
    #                 ucetnizaverkastmt = (insert(ucetnizaverka_).values(ico = int(item["ico"]) ,id_zaverka= a))
    #                 self.conn.execute(ucetnizaverkastmt)
    #     except KeyError:
    #             pass

    #     return item
    
    def process_item(self, item, spider):       
       
          # calling dumps to create json data.
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"  
        self.file.write(line)               
        return item
 
    def open_spider(self, spider):
        self.file = open('result.json', 'w')
 
    def close_spider(self, spider):
        self.file.close()