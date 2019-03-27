import csv
import os
import collections
months =[]
revenue =[]
TotalRevenue=[]

budgetDataList=['budget_data_1','budget_data_2']

for eachBudgetDataBook in budgetDataList:
    budgetCSV=os.path.join(eachBudgetDataBook+'.csv')
#csvpath = os.path.join("Resources", "budget_data_1.csv")

with open(budgetCSV, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    sum =0
    count=0
    for row in csvreader:
        if row[0] not in months:
            months.append(row[0])
            count = count+1
            
        revenue.append(row[1])
        sum = sum+(float(row[1]))
        TotalRevenue.append(sum)
        AverageRevenue= round(sum/count)
        find=max(revenue)
        find1=min(revenue)

    print("Finanicial Analysis")
    print("----------------------") 
    print("Total Months:",count)         
    print("Total Revenue:","$",sum)
    print("Average Revenue:" , "$",AverageRevenue)
    print("Greatest Increase in Revenue:","(",'$',find,")")  
    print("Greatest Decrease in Revenue:","(",'$',find1,")")
   


