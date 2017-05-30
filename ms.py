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

days = []
now = datetime.datetime.now()
days.append(now.strftime('%d'))
today = now.strftime('%Y%m%d')
tomorrow = now + datetime.timedelta(days=1)
days.append(tomorrow.strftime('%d'))
thedayafter = now + datetime.timedelta(days=2)
days.append(thedayafter.strftime('%d'))
afterthedayafter = now + datetime.timedelta(days=3)
days.append(afterthedayafter.strftime('%d'))

epoch_times = []
epoch_today = str(time.mktime(now.timetuple()))[:10]
epoch_times.append(epoch_today)
epoch_tomorrow = str(time.mktime(tomorrow.timetuple()))[:10]
epoch_times.append(epoch_tomorrow)
epoch_thedayafter = str(time.mktime(thedayafter.timetuple()))[:10]
epoch_times.append(epoch_thedayafter)
epoch_afterthedayafter = str(time.mktime(afterthedayafter.timetuple()))[:10]
epoch_times.append(epoch_afterthedayafter)

start_epoch = str(time.mktime(now.timetuple()))[:10]
end_epoch = str(time.mktime(thedayafter.timetuple()))[:10]
#epoch = datetime.datetime.utcfromtimestamp(0)

host = base64.b64decode("aHR0cDovL21vdmllc3Rhci5iZy8=")
headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36" , "Referer": host}
url_template = "%s?rhc_action=get_calendar_events&post_type[]=events&start=%s&end=%s&rhc_shrink=0&view=agendaDay"

### Iterate days
for i in range(0, 3):
  url = url_template % (host, epoch_times[i], epoch_times[i+1])
  print "Getting url: %s " % url
  r = requests.get(url, headers=headers)
  print "Server response: %s " % r.status_code

  if not os.path.exists("moviestar"):
    os.makedirs("moviestar")
    
  file_name = "moviestar/%s.json" % days[i]
  with open(file_name, "w") as f:
    f.write(r.text[3:].encode("utf-8"))

  items = json.load(codecs.open(file_name, 'r', 'utf-8-sig'))
  
  programs = []
  
  for item in items["EVENTS"]:
    rdates = item["fc_rdate"].split(",")
    for rdate in rdates:
      if today in rdate or tomorrow.strftime('%Y%m%d') in rdate:
        
        title = normalize(item["title"])        
        starttime = rdate[9:11]+":"+rdate[11:13]
        program = Program(starttime, title)
        
        program.url = item["url"]
        program.datetime = rdate.replace("T", "")
        programs.append(program)
  
  print "Sorting"
  programs_sorted = sorted(programs, key=lambda m: m.datetime, reverse=False)
  
  get_movie_details = True
  if (get_movie_details):
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
  
  with open(file_name, "w") as f:
    f.write(pretty_json(programs))
