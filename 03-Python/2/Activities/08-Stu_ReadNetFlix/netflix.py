# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("Resources", "netflix_ratings.csv")

# Bonus
# ------------------------------------------
# Set variable to check if we found the video
# Try: Zootopia; Gossip Girl
found = False

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if row[0].lower() == video.lower():
            print(row[0]+ " is rated "+ row[1] + " with a rating of " + row[6])
            found = True
            break

    # If the video is never found, alert the user
    if found == False:
        print("Sorry about this, we don't seem to have what you are looking for!")
