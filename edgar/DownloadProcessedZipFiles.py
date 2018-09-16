# Generate the list of index files archived in EDGAR since start_year (earliest: 1993) until the most recent quarter
import datetime
 
import requests
import io
import zipfile
import os
import sys

year = sys.argv[1]
quarter = sys.argv[2]

outputDir = '.\%s%s' % (year , quarter)

if not os.path.exists(outputDir):
    os.mkdir(outputDir)

zipFileName = '%s%s.zip' % (year , quarter)

url = 'https://www.sec.gov/files/dera/data/financial-statement-data-sets/' + zipFileName
print(url)
print(zipFileName)

resp_head = requests.head(url, allow_redirects=True)
if(resp_head.status_code == requests.codes.ok):
    results = requests.get(url, stream=True)
    z = zipfile.ZipFile(io.BytesIO(results.content))
    z.extractall(outputDir)
else:
    print ("file for %s %s at url %s does not exist" % (year, quarter, url))
    print(resp_head)

 
