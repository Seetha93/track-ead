import csv
import codecs

case = {}
date = {}
with open('./status-13-July.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if(row[1] != 'Status'):
            if(row[0] not in case):
                case[row[0]] = {}
            case[row[0]] = row[1].replace("[", "").replace("]","").replace('\'', '')
            date[row[0]] = row[2]

changed = {}
with open('./status-14-July.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if(row[1] != 'Status'):
            if(row[0] not in case):
                row[0] = {}
            else:
                if row[1].replace("[", "").replace("]","").replace('\'', '') != case[row[0]] and case[row[0]] == 'Case Was Received':
                    changed[row[0]] = {}
                    changed[row[0]]['old'] = case[row[0]]
                    changed[row[0]]['new'] = row[1].replace("[", "").replace("]","").replace('\'', '')
                    changed[row[0]]['receivedDate'] = date[row[0]]
            
with codecs.open('./13-14-delta.csv', 'w', encoding='utf8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([
            'Case', 
            'Old-Status',
            'New-Status',
            'Received-Date'
        ])
        for case in changed:
            csv_writer.writerow([case, changed[case]['old'], changed[case]['new'], changed[case]['receivedDate']])
        csv_writer.writerow([])    