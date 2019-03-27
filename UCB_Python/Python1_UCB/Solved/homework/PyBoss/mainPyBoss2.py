
import csv
import os
import re
from datetime import datetime
from datetime import date

employee_data1CSV = os.path.join('employee_data2.csv')
#employeeWorkBooks=['employee_data1','employee_data2']

#for eachEmployeeBook in employeeWorkBooks:

    #employeeCSV= os.path.join(eachEmployeeBook +'.csv')
    #Newemployee_data1CSV = os.path.join('outputPyBank',eachEmployeeBook +'.csv')

Emp_Id = []
Emp_Name =[]
First_Name = []
Last_Name = []
DOB_new =[]
dateList=[]
SSN = []
Statevariable =[]
States=[]
StateDict = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO',
    'Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL',
    'Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME','Maryland': 'MD',
    'Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT',
    'Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY',
    'North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA',
    'Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT',
    'Vermont': 'VT','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI',
    'Wyoming': 'WY',}


#reading employee_data1CSV file
with open (employee_data1CSV,'r') as csvfile:
     csvreader=csv.reader(csvfile, delimiter=',')
     next(csvreader,None)

     for row in csvreader:
         Emp_Id.append(row[0])

         Emp_Name.append(row[1])         
         Emp_Name = row[1].split(" ")
         First_Name.append(Emp_Name[0])
         Last_Name.append(Emp_Name[1])

    #COnverting date foramt to %m/%d/%Y
         DOB= datetime.strptime(row[2],'%Y-%m-%d')
         DOB_new=DOB.strftime('%m/%d/%Y') 
         dateList.append(DOB_new)

    #Re writing SSN number
         ssnNumber= re.sub('[0-9]','*',row[3],5)
         SSN.append(ssnNumber)

    #Re writing states to state abberivation using dictionaries     
         StateVariable=StateDict[row[4]]
         States.append(StateVariable)


cleaned_csv= zip(Emp_Id,First_Name,Last_Name,dateList,SSN,States) 

#Creating output csv file:test3.csv
newEmpOutput_file = os.path.join("OutputNewEmpBook2.csv")

#Writing records to test3.csv file
with open(newEmpOutput_file, "w",newline="") as datafile:
     writer = csv.writer(datafile)
     writer.writerow(["Emp_Id","First Name","Last Name","DOB","SSN","State"])  

     writer.writerows(cleaned_csv)        
     