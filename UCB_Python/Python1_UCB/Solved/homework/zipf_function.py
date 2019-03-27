#numberlist1=[1,2,3]
#stringlist=["one","two","three","four","five"]
#count = stringlist.count('one')
#result = zip(numberlist1,stringlist)
#print(result)
#resultset= set(result)
#print(resultset)
#print(count)
import csv
import os

total =[]
#count1=0
csvpath = os.path.join("election_data_1.csv")
#clist1 = ["Seth", "Vestal", "Torres", "Cordin"]

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvreader1 = csv.reader(csvfile, delimiter=',')
    Candidate =[]
    next(csvfile)
    #print(csvreader)
    
    count =0
    count1=0
    count2=0
    count3=0
    count4=0
    for row in csvreader:
       # row[2]=0
        
        #Candidate.append(row[2])
        if row[2] not in Candidate:
            Candidate.append(row[2])
            count = count+1
        if row[2] == Candidate[0]:
            count1=count1+1 
        elif row[2] == Candidate[1]:
            count2=count2+1 
        elif row[2] == Candidate[2]:
            count3=count3+1       
        elif row[2] == Candidate[3]:
            count4=count4+1 
      
    print(len(Candidate))
            
    print("Candidate Name:----:",Candidate)     
    print('',Candidate[0],":",count1,'\n',Candidate[1],":",count2,'\n',Candidate[2],":",count3,'\n',Candidate[3],":",count4) 
   
  
     #for k,v in name.items():
         #print(k,v)
    # for key1,Candidate in name.items():
    #    
    #     for attribute1,value1 in name.items():
    #         print("",'{}:  {}'.format(attribute1,value1))   
      

      
