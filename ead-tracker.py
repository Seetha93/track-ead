import sys
import requests
import lxml.html as lh
import csv
import codecs
import re
from tqdm import tqdm



def status_checker(case_number, genre):
    url = 'https://egov.uscis.gov/casestatus/mycasestatus.do'
    
    form_data = {
        'changeLocale': '',
        'appReceiptNum': case_number,
        'initCaseSearch': 'CHECK+STATUS',
    }

    response = requests.post(url, data=form_data)

    tree = lh.document_fromstring(response.content)

    # print tree.xpath("/html/body/div[2]/form/div/div[1]/div/div/div[2]/div[3]/h1/text()")
    return tree.xpath("/html/body/div[2]/form/div/div[1]/div/div/div[2]/div[3]/h1/text()")


if __name__ == '__main__':
    with codecs.open('./status-28-June.csv', 'w', encoding='utf8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([
            'Case Number', 
            'Status'
        ])
        for x in tqdm(range(1000)):
            if x < 10:
                case_number = sys.argv[1]+'00'+str(x)
            if x >= 10 and x < 100:
                case_number = sys.argv[1]+'0'+str(x)
            if x >= 100 and x < 1000:
                # print 'YSC1990227'+str(x)
                case_number = sys.argv[1]+str(x)
            status = status_checker(case_number, 'status')
            csv_writer.writerow([case_number, status])
    