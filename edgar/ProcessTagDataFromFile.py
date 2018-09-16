import io
import os
import csv
import sys
import ceODBC

year = sys.argv[1]
quarter = sys.argv[2]

# Download index files and write content into SQLite
import pypyodbc
#connection = pypyodbc.connect('Driver={SQL Server};Server=PRAMENDRA-PC\SQLEXPRESS01;Database=edgar;Trusted_Connection=yes;')
connection = ceODBC.connect('Driver={SQL Server};Server=PRAMENDRA-PC\SQLEXPRESS01;Database=edgar;Trusted_Connection=yes;', autocommit = True)
cur = connection.cursor()
cur.execute("if not exists (select * from sysobjects where name='XBRLTaxonomyTags' and xtype='U') CREATE TABLE XBRLTaxonomyTags (tag varchar(512),	version varchar(40), custom varchar(2),abstract varchar(2), datatype varchar(40),	iord varchar(2),crdr varchar(2), tlabel varchar(1024),	doc varchar(4096))")

outputDir = '%s%s' % (year , quarter)

# numTxtFile = '.\%s\\num.txt' % (outputDir)
# preTxtFile = '.\%s\\pre.txt' % (outputDir)
# subTxtFile = '.\%s\\sub.txt' % (outputDir)
tagTxtFile = '.\%s\\tag.txt' % (outputDir)

print(outputDir)
print(tagTxtFile)

# TODO: Exit with error if the num.txt file does not exist

#process num.txt.file
with open(tagTxtFile , newline='', encoding='latin-1') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    columns = next(reader) 
    print(','.join(columns))
    
    # precreate table
    # tag varchar(512), version varchar(200), custom varchar(2),abstract
    # varchar(2), datatype varchar(20), iord varchar(2),crdr varchar(2), tlabel
    # varchar(1024), doc varchar(3000)

    for line in reader:
        cursor = connection.cursor()
        for data in reader:
            (tag, version, custom, abstract, datatype, iord, crdr, tlabel, doc) = data
            params = (tag, version, custom, abstract, datatype, iord, crdr, tlabel, doc)
            cursor.execute("{CALL dbo.InsertTag (?,?,?,?,?,?,?,?,?)}", params)
        cursor.commit()
connection.close()
 
