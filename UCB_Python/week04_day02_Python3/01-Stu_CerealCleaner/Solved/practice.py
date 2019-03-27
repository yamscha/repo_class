import csv
import os

cereal_csv_path = os.path.join("..","Resources","cereal_bonus.csv")

with open(cereal_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =",")
    next(csv_reader, None)

    for row in csv_reader:
        if (float(row[7]) >=5):
            print(row)

