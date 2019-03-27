import os
import csv

cereal_csv_path = os.path.join("..", "Resources", "cereal_bonus.csv")

with open(cereal_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip the first row of the csv
    #why do we put None as a second argument to next()?
    #Let's ask the internet!
    #https://docs.python.org/2/library/functions.html#next
    next(csv_reader, None)

    # Loop through rows
    for row in csv_reader:

        # Convert row to float and compare to grams of fiber
        if float(row[7]) >=5:
            print(row)
