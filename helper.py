import json

def normalize(txt):
  return txt.lstrip().rstrip().replace("\"", "\\\"").capitalize()
  
def pretty_json(src):
  return json.dumps(src,indent=2, separators=(',', ': ')).decode('unicode-escape').encode('utf8')
  
def log(msg):
  print "### %s" % msg
  logFile.write("%s\n" % msg)
  
logFile = open("log.txt", "w")
  
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
