#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys
import json
import time
import base64
import codecs
import datetime
import requests
from helper import *

reload(sys)
sys.setdefaultencoding('utf-8')

DEBUG = False
STARTDAY = 3 #start capturing 3 days ahead
MAXDAYS = 1
channel = "dusk"
host = base64.b64decode("aHR0cHM6Ly93d3cuZHVzay10di5jb20v")
headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36" , "Referer": host}
url_template = "%sapi/tvguides?date=%s&home_view=false&language=en&limit=999"

### Calculate dates for for scrabbing days
dates = get_dates(MAXDAYS, STARTDAY)

### Iterate days
for i in range(0, MAXDAYS):
  url = url_template % (host, dates[i].datetime_hyphened)
  file_name = get_file_name(channel, dates[i].day)

  r = requests.get(url, headers=headers)
  items = r.json()["data"]
  
  programs = []
  programs_sorted = []
  
  for item in items:
    title = normalize(item["name"]).capitalize()
    starttime = re.compile("(\d\d:\d\d):").findall(item["starttime"])[0]
    program = Program(starttime, title)
    try:
      program.description = normalize(item["description"])
      program.icon = item["screenshot"]
      program.year = item["jaar"]    
    except Exception as er:
      print str(er)
    programs.append(program)
  
  write_file(file_name, programs)