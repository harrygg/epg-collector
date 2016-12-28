#!/usr/bin/env python
# -*- coding: utf8 -*-
import os, sys
import xml.etree.ElementTree as ET
from ids import *
from helper import *

log("ENVIRONMENT: %s" % os.environ)
### OPTIONS
SHORTEN_DESC = False#512             # Set False to disable
OUTPUT_XML = 'epg.xml' # Output XML name
errors = 0
xmlName = False
forced = len(sys.argv) > 1 and sys.argv[1] == "-f"

### URLs and output files
#{"url":"https://dl.dropboxusercontent.com/s/xg6c7av61p1jdoq/epg.xml.gz", "outFile":"bulgarian-guide.xml.gz"},
epgs = [
  {"url":"http://sov02lr02.eu.hpecorp.net/guides/bulgarian/epg.xml", "outFile": "my-bg-guide.xml"},
  {"url":"http://sov02lr02.eu.hpecorp.net/guides/movies/rex/epg.xml", "outFile": "my-guide.xml"},
  {"url":"http://sov02lr02.eu.hpecorp.net/guides/sports/epg.xml", "outFile": "my-sports-guide.xml"},
  {"url":"http://sov02lr02.eu.hpecorp.net/guides/deutsch/epg.xml", "outFile": "my-deutsch-guide.xml"},
  {"url":"http://epg.tvsat.co/epg.xml.gz", "outFile":"bulgarian-guide.xml.gz"},
  {"url":"http://doubledmusic.eu/tivibg/guide.xml", "outFile":"bulgarian-guide2.xml"},
  {"url":"http://www.teleguide.info/download/new3/xmltv.xml.gz", "outFile":"russian-guide.xml.gz"},
  {"url":"http://epg.serbianforum.org/epg.xml.gz", "outFile":"serbian-guide.xml.gz"},
]

epgFiles = []

### Logic
log("#############################\nEPG COLLECTOR\n#########################")

try:
  # Download EPGs
  log("Forced download = %s" % forced)
  for e in epgs:
    out_file_name = e["outFile"]
    ## Is file old enough
    if isExpired(out_file_name) or forced:
      download(e["url"], out_file_name)
    else:
      log("%s is new, download skipped!" % out_file_name)
    
    ## If file is zipped, extract and get extracted's file name
    if 'gz' in out_file_name:
      xmlName = extract(out_file_name)
    else:
      xmlName = out_file_name
    ##False if there was error
    if xmlName:
      log("  Adding %s to epgFiles[]" % xmlName)
      epgFiles.append(xmlName)
    else: 
      log("  Trying re-download")
      download(e["url"], out_file_name) #If there is an error during extract, file maybe corrupted so try re-downloading the file
      ## If file is zipped, extract and get extracted's file name
      if '.gz' in out_file_name:
        xmlName = extract(out_file_name)
      else:
        xmlName = out_file_name

      if xmlName:
        epgFiles.append(xmlName)
      else:
        errors += 1
        log("Still unable to extract file %s. Skipping" % out_file_name)

  #Build EPG files 
  log("\n### Parsing started for %s files!" % len(epgFiles))
  n = 0
  for f in epgFiles:
    if 'russian' in f or 'my' in f: #Get ids from <channel-name> tag in XMLTV
      d = parse(f, True) 
    else:
      d = parse(f)
    log("------------------------------")
    log("  Extracted %s channels" % d)
    log("------------------------------")
    n += d
  
  #zip epg file
  #log("Zipping XML file to %s" % OUTPUT_XML + ".gz")
  #zip(OUTPUT_XML, OUTPUT_XML + ".gz")
  
except KeyboardInterrupt:
  log('EPG generation interrupted by user!')
except Exception, er:
  import traceback
  log(traceback.print_exc())

### Save the new EPG
tree = ET.ElementTree(xmltv)
tree.write(OUTPUT_XML, encoding="UTF-8", xml_declaration=True)

file_info = os.stat(OUTPUT_XML)
log("%s channels saved in file %s (%s)" % (n, OUTPUT_XML, convert_bytes(file_info.st_size)))
logFile.close()
