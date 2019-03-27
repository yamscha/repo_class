import csv
import os

#creating electiondatalist 
electionDataList=['election_data_1','election_data_2']

#loop through electiondatalist
for eachElectionBook in electionDataList:

    electionCSV = os.path.join(eachElectionBook+'.csv')

with open(electionCSV, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
   
     Candidate =[]
     next(csvfile)
     count =0
     eachCandidate=dict()
     votesTotal =0

     for row in csvreader:
          
         if row[2] not in Candidate:
            Candidate.append(row[2])
            count = count+1
         if row[2] not in eachCandidate:
            eachCandidate[row[2]] = 1
         else:
            eachCandidate[row[2]]= eachCandidate[row[2]] + 1

         votesTotal = votesTotal + 1

              
     print("Total Votes :", votesTotal) 
     print("--------------------------------")      
     
     for key in eachCandidate:

         x = round(eachCandidate[key]/votesTotal*100,2)
         print (key,":"," ",eachCandidate[key],"  ",'(',x,'%',')')
        
         if eachCandidate[key] > 1370000:
            name=key
     print("--------------------------------")        
     print("Winner: ", name)    

     print("--------------------------------")    


    
    
