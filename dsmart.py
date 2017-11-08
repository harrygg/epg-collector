import requests
import datetime
import sys
import os
from helper import *
from bs4 import BeautifulSoup

reload(sys)  
sys.setdefaultencoding('utf8')

DEBUG = False
STARTDAY = 0 #start capturing 3 days ahead
MAXDAYS = 3
dates = get_dates(MAXDAYS, STARTDAY)
#Semerkand, NR1 TV
channels = [{"id":"58d29bb0eefad3db9c60627c", "name":"Semerkand"}, {"id": "58d29bb0eefad3db9c60623c", "name":"NR1 TV"}]

for channel in channels:
  for date in dates:
    url = "https://www.dsmart.com.tr/actions/schedule?channel_id=%s&day=%s" % (channel["id"], date.datetime_hyphened)
    text = get_content(url)
    dir = channel["name"].lower().replace(" ", "")
    file_name = get_file_name(dir, date.day)
    print "Saving %s" % (file_name)
    with open(file_name, "w") as w:
      w.write(text)

  write_index(dir)