import requests
import datetime
import sys
import os
from helper import *
from bs4 import BeautifulSoup

reload(sys)  
sys.setdefaultencoding('utf8')

parts = ["n", "v", "m", "a"]

DEBUG = False
STARTDAY = 0 #start capturing 3 days ahead
MAXDAYS = 3
dates = get_dates(MAXDAYS, STARTDAY)
channels = ["sport1plus", "sport1us", "sport1tv"]
last_show_time = "" #hold the times so that we can check for duplicates

for channel in channels:
 
  for date in dates:
    
    first_part = True
    programs = []
    for part in parts:
      url = "http://tv.sport1.de/programm/wochenprogramm/index.php?d=%s&z=%s" % (date.datetime, part)
      soup = get_soup(url)
      
      print "Searching for element with id %s" % "epg_col_%s" % channel
      col = soup.find(id="epg_col_%s" % channel)
      print "Searching for elements with class epgItem"
      divs = col.find_all(class_="epgItem")
      print "%s elements found" % len(divs)
      
      #Remove the first show which is always from yesterday.
      #It causes issues
      if first_part:
        print "Removing first show of the day as it is always yesterday's"
        divs.pop(0)
        first_part = False
        
      for div in divs:
        
        try:
          ###########
          ### TIME
          ###########
          time = div.find("span", class_="time").get_text()
          if time == last_show_time:
            print "Program with the same time already added".encode("utf-8")
            continue
          last_show_time = time
          
          ############
          ### Title
          ############
          title = normalize(div.find("span", class_="title").renderContents())
          
          ### Crete the program object only after we have time and title
          program = Program(time, title)
          
          try: 
            program.subtitle = normalize(div.find("div", class_="epgSubtitle").get_text())
          except: pass
          
          ###############
          ### Description
          ###############
          try: 
            program.description = normalize(div.find("p", class_="text").get_text(separator=u'. '))
          except: pass
          
          programs.append(program)
        except:
          pass
      
    file_name = get_file_name(channel, date.day)
    write_file(file_name, programs)
