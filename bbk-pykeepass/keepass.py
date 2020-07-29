#!/usr/bin/python

from pykeepass import PyKeePass
import sys, getopt
import select
import os

if select.select([sys.stdin,],[],[],0.0)[0]:
    print("Have data!")
else:
    print("No data")
    sys.exit()
    
# load database
kp = PyKeePass('db.kdbx', password=os.environ['PASSWORD'])
group = kp.find_groups(name='Internet', first=True)

for line in sys.stdin:
   # Dateiinput trennen nach ";;;" und in einem Array speichern
   data = line.split(';;;')
   # Letztes Zeichen (\n) löschen
   data[-1] = data[-1].strip()
   
   # Hat das Array genau 4 Einträge?
   if len(data) != 4:
      print("Fehlerhafte Eingabe!")
      print(data)
      sys.exit()
      
   if data[0] == "EOF":
      break
   
   # Variablen setzen
   title = str(data[0])
   user = str(data[1])
   password = str(data[2])
   notes = str(data[3])
   
   # Eintrag in KeePassDB schreiben (temporär, nicht gespeichert)
   kp.add_entry(group, title, user, password, None, notes)
   
kp.save()
   
sys.exit()

# Print total number of arguments
#params = len(sys.argv)
#print ('Total number of arguments:', params)

#if params != 5:
#	print(sys.argv[0], "title user password notes")
#	sys.exit()
#else:
#	# Print all arguments
#	print ('Argument List:', str(sys.argv))

#title = str(sys.argv[1])
#user = str(sys.argv[2])
#password = str(sys.argv[3])
#notes = str(sys.argv[4])
