import os
import csv
wrestlingYears = ['2017', '2016', '2015', '2014']
#Always ask yourself if there is a better way, and then ask the internet!
#In my opinion, csv.DictReader is easier to work with than csv.Reader
for yearToCheck in wrestlingYears:
    #input file name 
    wrestlingCSV = os.path.join('..', 'raw_data', 'WWE-Data-' + yearToCheck + '.csv')
    #output file name
    newWrestlingCSV = os.path.join('..', 'output2', 'WWE-Data-' + yearToCheck + '.csv')
    with open(wrestlingCSV, 'r') as f_in, open(newWrestlingCSV, 'w') as f_out:
        d_reader = csv.DictReader(f_in)
        fieldnames=['Wrestler','Wins','Losses','Draws','total','win %','loss %','draw %']
        d_writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        d_writer.writeheader()
        #save memory! extract, transform, then load
        for record in d_reader:
            record['total'] = int(record['Wins']) + int(record['Losses']) + int(record['Draws']) 
            record['win %'] = int(record['Wins'])/record['total'] * 100
            record['loss %'] = int(record['Losses'])/record['total'] * 100
            record['draw %'] = int(record['Draws'])/record['total'] * 100
            d_writer.writerow(record)
