import json
import datetime
import requests
import time
import os
from bs4 import BeautifulSoup

def normalize(txt):
  return txt.lstrip().rstrip().replace("\"", "\\\"").replace("\\n","")
  
def pretty_json(programs):
  converted = [p.__dict__ for p in programs]
  print "Sorting"
  programs_sorted = sorted(converted, key=lambda p: p["starttime"], reverse=False)
  return json.dumps(programs_sorted,indent=2, separators=(',', ': ')).decode('unicode-escape').encode('utf8')

def append_hours(hour, n):
  hour = datetime.strptime(hour, "%H")
  hour += timedelta(hours=n)
  return str(hour)

def log(msg):
  print "### %s" % msg
  logFile.write("%s\n" % msg)
  
logFile = open("log.txt", "w")

__headers__ = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}

def get_soup(url, headers=None):
  global __headers__
  if headers:
    __headers__ = headers
    
  print "Requesting url: %s" % url
  r = requests.get(url, headers=__headers__)
  soup = BeautifulSoup(r.text, 'html.parser')
  ### save response
  if False:
    try: 
      with open("last_response.html", "w") as w: 
        w.write(r.text) 
    except: pass
  return soup

def get_content(url, headers=None):
  global __headers__  
  if headers:
    __headers__ = headers
  print "Requesting url: %s" % url
  r = requests.get(url, headers=__headers__)
  print "Server response: %s " % r.status_code
  ### save response
  if False:
    try: 
      with open("last_response.html", "w") as w: 
        w.write(r.text) 
    except: pass
  return r.text

def get_file_name(results_folder, day):
  if not os.path.exists(results_folder):
    os.makedirs(results_folder)
  return "%s/%s.json" % (results_folder, day)

def write_file(file_name, programs):
  print "Saving %s programs in %s" % (len(programs), file_name)
  with open(file_name, "w") as f:
    f.write(pretty_json(programs))

class Program():
  
  starttime = ""
  title = ""
  subtitle = ""
  titleOriginal = ""
  category = ""
  icon = ""
  description = ""
  cast = ""
  director = ""
  year = ""
  country = ""
  rating = ""
  url = ""
  day = ""
  datetime = ""
  
  def __init__(self, starttime, title):
    
    if not ":" in starttime or not starttime.replace(":", "").isdigit():
      msg = "startime must have the proper format 00:00"
      print msg
      Exception(msg)
      
    self.starttime = starttime
    print "Inializing new Program object"
    print "startime=%s" % starttime
    self.title = title
    print "title=%s" % title

def get_dates(MAXDAYS=3, STARTDAY=0):
  dates = []
  now = datetime.datetime.now()
  end = MAXDAYS + 1 # get an extra day epoch time as a limit for previous day
  for i in range(0, end):
    offset = STARTDAY + i
    current_day = now + datetime.timedelta(days=offset)
    date = Date(current_day)
    dates.append(date)
  return dates
    
class Date():
  def __init__(self, current_day):
      self.datetime = current_day.strftime('%Y%m%d')
      self.datetime_hyphened = current_day.strftime('%Y-%m-%d')
      self.day = current_day.strftime('%d')
      self.epochtime = str(time.mktime(current_day.timetuple()))[:10]