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
channels = ["58d29bb0eefad3db9c60627c", "58d29bb0eefad3db9c60623c"]

for channel in channels:
  for date in dates:
    url = "https://www.dsmart.com.tr/actions/schedule?channel_id=%s&day=%s" % (channel, date.datetime_hyphened)
    text = get_content(url)
    file_name = get_file_name(channel, date.day)
    write_file(file_name, programs)