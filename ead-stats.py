import csv
import codecs
import re
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

statuses = {}
with open('./status-28-June.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if(row[1] != 'Status'):
            if(row[1].replace("[", "").replace("]","").replace('\'', '') not in statuses):
                statuses[row[1].replace("[", "").replace("]","").replace('\'', '')] = 1
            else:
                statuses[row[1].replace("[", "").replace("]","").replace('\'', '')] = statuses[row[1].replace("[", "").replace("]","").replace('\'', '')] + 1

with codecs.open('./daily-stats.csv', 'a', encoding='utf8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([
            'Status', 
            'Count'
        ])
        for status in statuses:
            csv_writer.writerow([status, statuses[status]])
        csv_writer.writerow([])
