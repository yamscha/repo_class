import os
import csv
udemy_csv = os.path.join("Resourses", "WebDevelopment.csv")

title = []
price = []
subscriber_count = []
reviews = []
length = []
review_percent = []

with open (udemy_csv, newline="") as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        #Adding title
        title.append(row[1])

        #Add price

        price.append(row[4])

        # Add subcount

        subscriber_count.append(row[5])

        reviews.append(row[6])

        percent =round(int(row[6])/int(row[5]),2)
        review_percent.append(percent)

        new_length=  row[9].split(" ")
        length.append(new_length[0])

cleaned_csv= zip(title, price, subscriber_count, reviews, length, review_percent)  
   
output_file =os.path.join("web_finals.csv")

 #open the output file
with open(output_file,"w", newline="") as datafile:
    writer=csv.writer(datafile)

    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])    
 #write in Zippped rows
    writer.writerows(cleaned_csv)

    







