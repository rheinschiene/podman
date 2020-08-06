#!/usr/bin/python

from pykeepass import PyKeePass
import sys, getopt
import select
import os
import pathlib

groupname = os.environ['GROUPNAME']
tempfile = os.environ['TEMPFILE']
dbfile = os.environ['DBFILE']

path = pathlib.Path(tempfile)
if not path.is_file():
   print("Datei fehlt: " + tempfile)
   sys.exit()
   
path = pathlib.Path(dbfile)
if not path.is_file():
   print("Datei fehlt: " + dbfile)
   sys.exit()
    
# load database
kp = PyKeePass(dbfile, password=os.environ['PASSWORD'])
group = kp.find_groups(name=groupname, first=True)

count = 1
with open (tempfile, "r") as rd:
   # Read lines in loop
   for line in rd:
      # All lines (besides the last) will include  newline, so strip it
      data = line.strip()
      data = data.split(';;;')

      if len(data) != 4:
         print("Fehlerhafte Eingabe! Zeile: " + str(count))
         print(data)
         sys.exit()
         
      # Variablen setzen
      title = str(data[0])
      user = str(data[1])
      password = str(data[2])
      notes = str(data[3])
   
      # Eintrag in KeePassDB schreiben (temporär, nicht gespeichert)
      kp.add_entry(group, title, user, password, None, notes)
      count += 1
   
kp.save()
   
sys.exit()
