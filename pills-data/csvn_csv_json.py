import csv
import json

csvfile = open('pillbox.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("id", "spl_id","SETID","spp", "NDC9", "PRODUCT_CODE","EQUAL_PRODUCT_CODE",
              "author", "SPLIMPRINT" ,"SPLCOLOR" ,"SPLSHAPE", "SPLSIZE" ,"SPLSCORE" ,"DEA_SCHEDULE_CODE",
              "INGREDIENTS", "SPL_INACTIVE_ING", "RXCUI,RXTTY", "RXSTRING", "image_id", "IMAGE_SOURCE",
              "HAS_IMAGE","FROM_SIS","NO_RXCUI")

reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')