import os
import sys
import json
import datetime
import requests
from bs4 import BeautifulSoup
from helper import *

reload(sys)  
sys.setdefaultencoding('utf8')

date = datetime.date.today()
day = int(date.strftime('%d'))
channels = ["history", "crime-investigation"]#, "h2"]
hours = ["00", "02", "04", "06", "08", "10", "12", "14", "16", "18", "20", "22"]

headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
url_template = "http://www.historytvbulgaria.com/bg/%s-bg?epgnav=%s&epgweekview=1"

days = []#{"datetime":None, "shows":list()}] * 7 #Create an empty list with 7 elements
#print days

for channel in channels:
  for hour in hours:
    print "---------------------------------------------"
    date_str = "%s%s0000" % (date.strftime('%Y%m%d'), hour)
    url = url_template % (channel, date_str)
    print "Requesting url: %s" % url
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
  
    ### save last response
    try:
      with open("last_response.%s.html" % channel, "w") as w: 
        w.write(r.text) 
    except: 
      pass
    
    epg_data_days = soup.find_all(class_="epg-data-row-normal") # returns 7 elements
    print "Found program for %s days" % len(epg_data_days)
    
    ### Iteratate days - 7
    for i in range(0, len(epg_data_days)):
  
      day_str = date.strftime('%Y%m')
      day_str += epg_data_days[i].find("p", "text-large").get_text().split("/")[0]
      
      # Add only datetime tag during first 7 days
      if len(days)  < len(epg_data_days):
        days.append({"datetime":day_str, "shows":[]})
      
      print "Scrabbing day %s" % i
      epg_daily_programs = epg_data_days[i].find_all(class_="epg-data-cell")
      
      for epg_program in epg_daily_programs:        
        ### Get show start time
        txt = epg_program.find("small").get_text().split(" - ")[0]
        starttime = normalize(txt)
        ### Get show title
        txt = epg_program.find("h4", class_="schedule-show-title").get_text()
        title = normalize(txt)
        ### We initialize only if starttime and title exist
        program = Program(starttime, title)
        
        ### Get subtitle
        try:
          txt = epg_program.find("div", class_="schedule-episode-title").get_text()
          program.subtitle = normalize(txt)
          print "subtitle=" + program.subtitle
        except:
          pass
        
        ### Get icon source
        try:
          id = epg_program["value"]
          print "id=" + id
          class_name = "epg-weekly-element-%s" % id
          extras_div = soup.find("div", class_=class_name)
          try:
            txt = extras_div.find("img")["src"]
            program.icon = txt
            print "icon=" + txt
          except:
            pass
          
          ### Get show description
          try:
            txt = extras_div.find("div", class_="show-summary").get_text()
            program.description = normalize(txt)
            print "desc=" + program.description
          except:
            pass
  
        except:
          pass
        
        ### Append current day program to days list if it's not already added
        if not any(show["starttime"] == program.starttime for show in days[i]["shows"]):
          print "Appending program to day %s" % (day + i)
          days[i]["shows"].append(program.__dict__)
        else:
          print "Program is a duplicate skipping it"

  print days
  ### Save weekly program
  if not os.path.exists(channel):
    os.makedirs(channel)
  
  with open("%s/weekly.json" % channel, "w") as f:
    f.write(json.dumps(days,indent=2, separators=(',', ': ')).decode('unicode-escape').encode('utf8'))

  ### Save daily programs   
  for d in days:
    with open("%s/%s.json" % (channel, d["datetime"][6:8]), "w") as f:
      f.write(pretty_json(d))
