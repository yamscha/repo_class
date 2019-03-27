
import csv 
import os
import re
from datetime import datetime
from datetime import date

name="yamini chandala"
firstname=[]
lastname=[]

ssnList=['234-01-8166','567-98-3234']
for ssn in ssnList:
    ssnNumber=(re.sub('[0-9]','*',ssn,5))
    print(ssnNumber)

s = name.split(" ")
firstname.append(s[0])
lastname.append(s[1])
dateList=['2016-01-12','2017-03-24']
newdateList=[]

#States
statedic={'Florida': 'FL','Colorado': 'CO'}

for key,value in statedic.items():
     print(value)

for y in dateList:
    dateobject = datetime.strptime(y,"%Y-%m-%d")
    convertedDateString = dateobject.strftime("%d/%m/%y")
    newdateList.append(convertedDateString)

cleaned_csv= zip(firstname,lastname,newdateList) 
output_file = os.path.join("test.csv")

#write output file
with open(output_file, "w",newline='') as datafile:
     writer = csv.writer(datafile, delimiter=',')
     for line in cleaned_csv:
         writer.writerow(line)
 
     