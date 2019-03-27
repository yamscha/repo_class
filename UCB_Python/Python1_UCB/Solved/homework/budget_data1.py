import csv
import os
import collections
months =[]
maximumlist=[]
total =[]
revenue =[]
findmonth=[]
csvpath = os.path.join("Resources", "budget_data_1.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    print(csvreader)
    sum =0
    count=0
    for row in csvreader:
        if row[0] not in months:
            months.append(row[0])
            count = count+1
            
        revenue.append(row[1])
        sum = sum+(float(row[1]))
        total.append(sum)
        average=sum/count
   
        
        find=max(revenue)
        
        find1=min(revenue)
                
    print("Total Revenue:",sum)
    print(count)  
    print("Average:" , average)
    print("max",row[0],find)  
    print("min",row[0],find1)
   

