#!/usr/bin/env python
# -*- coding: utf8 -*-

import os, sys, json
import xml.etree.ElementTree as ET

fileName = ""
if len(sys.argv) > 1:
  fileName = sys.argv[1]

path = os.path.dirname(fileName)
tree = ET.parse(fileName)
ids = []
channel_ids = []


for elem in tree.iter():
  if elem.tag == 'channel':
    id = elem.attrib["id"].decode('utf-8')
    print id
    ids.append(id)
    channel_ids.append(id.decode('utf-8'))

  if elem.tag == 'programme':
    cid = elem.attrib["channel"]
    try: ids.remove(cid)
    except: pass

f_output = os.path.join(path, 'validation.json')
n_missing = len(ids)
print "%s missing channels" % n_missing
data = {"total": len(channel_ids), "ids":channel_ids, "missing":n_missing, "missing_ids":ids}
with open(f_output, 'w') as w:
  json.dump(data, w)
