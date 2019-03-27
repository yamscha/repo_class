
import csv
import os
from datetime import datetime
from datetime import date

#grab employee data1 csv
#employee_data1CSV = os.path.join('..','raw-data','WWE-Data-','.csv')

employee_data1CSV = os.path.join('employee_data1.csv')


#create new CSV
#newEmployeeDataCSV=os.path.join('..','output','WWE-Data-','.csv')
#set empty list

Emp_Id = []
Emp_Name =[]
First_Name = []
Last_Name = []
#DOB = []
SSN = []
State = []
DOB_new =[]
Name=[]
dateList=[]
#nameSplit = name.split(" ")

#open current employee csv

with open(employee_data1CSV,'r') as csvfile:
     csvreader=csv.reader(csvfile, delimiter=',')
     next(csvreader,None)
     for row in csvreader:
         Emp_Id.append(row[0])
         Emp_Name.append(row[1])         
         Emp_Name = row[1].split(" ")
         First_Name.append(Emp_Name[0])
         Emp_Name=row[1].split(" ")
         Last_Name.append(Emp_Name[1])
         DOB= datetime.strptime(row[2],'%Y-%m-%d')
         DOB_new=DOB.strftime('%m/%d/%Y')
         dateList.append(DOB_new)
     
     
     #
     print (len(employee_data1.csv))


     print (Emp_Id[0],First_Name[0],Last_Name[0],dateList[0])     
         #cleaned_csv = (Emp_Id,First_Name,Last_Name, DOB_new)
         #list(cleaned_csv)

output_file = os.path.join("test2.csv")
#write output file
with open(output_file, "w",newline="") as datafile:
     writer = csv.writer(datafile)
     writer.writerow(["Emp_Id","Firstname","Lastname","New_DOB"])

     writer.writerows(cleaned_csv)


