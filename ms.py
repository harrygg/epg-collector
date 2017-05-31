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

MAXDAYS = 3
host = base64.b64decode("aHR0cDovL21vdmllc3Rhci5iZy8=")
headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36" , "Referer": host}
url_template = "%s?rhc_action=get_calendar_events&post_type[]=events&start=%s&end=%s&rhc_shrink=0&view=agendaDay"

### Calculate dates for for scrabbing days
dates = {"days":[], "datetimes":[], "epochtimes":[]}
now = datetime.datetime.now()
end = MAXDAYS + 1 # get an extra day epoch time as a limit for previous day
for i in range(0, end): 
  current_day = now + datetime.timedelta(days=i)
  dates["days"].append(current_day.strftime('%d'))
  dates["datetimes"].append(current_day.strftime('%Y%m%d'))
  #add epoch time i.e. 1496213915
  dates["epochtimes"].append(str(time.mktime(current_day.timetuple()))[:10])

if not os.path.exists("moviestar"):
  os.makedirs("moviestar")
    
### Iterate days
for i in range(0, MAXDAYS):
  url = url_template % (host, dates["epochtimes"][i], dates["epochtimes"][i+1])
  print "Getting url: %s " % url
  r = requests.get(url, headers=headers)
  print "Server response: %s " % r.status_code

  file_name = "moviestar/%s.json" % dates["days"][i]
  with open(file_name, "w") as f:
    f.write(r.text[3:].encode("utf-8"))

  items = json.load(codecs.open(file_name, 'r', 'utf-8-sig'))
  
  programs = []
  programs_sorted = []
  
  for item in items["EVENTS"]:
    rdates = item["fc_rdate"].split(",")
    for rdate in rdates:
      if dates["datetimes"][i] in rdate:
        
        title = normalize(item["title"])        
        starttime = rdate[9:11]+":"+rdate[11:13]
        program = Program(starttime, title)
        
        program.url = item["url"]
        program.datetime = rdate.replace("T", "")
        programs.append(program)
  
  print "Sorting"
  programs_sorted = sorted(programs, key=lambda p: p.datetime, reverse=False)
  
  debug = True
  if not debug:
    print "Searching for movie details"
    programs = []
    for program in programs_sorted:
      try:
        print "Requesting %s " % program.url
        r = requests.get(program.url, headers=headers)
        print "Response code %s" % r.status_code
        text = r.text.encode("utf-8")
    
        m = re.compile("og:description\"\s+content=\"(.*?)\"\s*/>").findall(text)
        if len(m) > 1:
          program.description = m[1]
          print "Description found!"
        elif len(m) == 1:
          program.description = m[0]
          
        m = re.compile("og:image:url\" content=\"(.*?)\"").findall(text)
        if len(m) > 0:
          program.icon = m[0]
          print "Icon found" 
      
        m = re.compile("<li><strong>Режисьор:</strong>(.*)</li>".encode("utf-8")).findall(text)
        if len(m) > 0:
          program.director = normalize(m[0])
          print "Director found"
          
        m = re.compile("<li><strong>.*?(\d\d\d\d).*?</strong>").findall(text)
        if len(m) > 0:
          program.year = m[0]
          print "Year found"
    
        m = re.compile("<li><strong>(\D*?)</strong></li>").findall(text)
        if len(m) > 0:
          program.category = normalize(m[0])
          print "Category found!"
    
        m = re.compile("<li><strong>\d\d\d\d\s(.+?)</strong>").findall(text)
        if len(m) > 0:
          program.country = normalize(m[0])
          print "Country found"
    
        m = re.compile("<li><strong>В ролите:.*?</strong>(.+?)</li>").findall(text)
        if len(m) > 0:
          program.cast = normalize(m[0])
          print "Cast found"
    
      except Exception as er:
        print str(er)
      
      del program.datetime
      programs.append(program.__dict__)
  
  if not debug:
    with open(file_name, "w") as f:
      f.write(pretty_json(programs))
