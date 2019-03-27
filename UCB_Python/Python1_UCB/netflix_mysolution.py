import csv
import os

video=input("What movie you are lokking for?")

#set path for file
csvpath = os.path.join("Resources","netflix_ratings.csv")

found = False

#open the csv file
with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    for row in csvreader:
        if row[0]==video:
            print(row[0]+ " is rated "+ row[1] + " with a rating of " + row[6])

            found = True

    if found == False:
        print("Sorry about this, we don't seem to have what you are looking for!")

