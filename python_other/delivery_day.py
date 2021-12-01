import holidays as hol
from datetime import datetime as dtm
import datetime
from datetime import timedelta

czhol = hol.CZ()

def is_weekend(inpar):
  return inpar.weekday() > 4



def delivery_day(deliveryday, orderday):

  start = 0

  startdate =  orderday


  while start < deliveryday:
      
      if startdate  not in czhol and  not is_weekend(startdate):
          start = start + 1
          startdate = startdate+ timedelta(days=1)
      else: 
          startdate = startdate+ timedelta(days=1)

  yr = int(startdate.strftime('%Y'))
  dt = int(startdate.strftime('%d'))
  mt = int(startdate.strftime('%m'))
  
  return datetime.date(yr,mt, dt)
