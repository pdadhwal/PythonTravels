import io
import os
import csv
import sys

year = sys.argv[1]
quarter = sys.argv[2]

# Download index files and write content into SQLite
import pypyodbc
connection = pypyodbc.connect('Driver={SQL Server};Server=PRAMENDRA-PC\SQLEXPRESS01;Database=edgar;Trusted_Connection=yes;')
cur = connection.cursor()

# precreate table
cur.execute("if not exists (select * from sysobjects where name='XBRLFactsNumeric' and xtype='U') CREATE TABLE XBRLFactsNumeric (adsh  varchar(40), tag  varchar(512), version  varchar(40), coreg  varchar(512), ddate char(8), qtrs  varchar(16), uom  varchar(40), value money, footnote  varchar(1024))")

outputDir = '%s%s' % (year , quarter)

numTxtFile = '.\%s\\num.txt' % (outputDir)

print(outputDir)
print(numTxtFile)

# TODO: Exit with error if the num.txt file does not exist

# adsh,tag, version, coreg, ddate , qtrs  , uom  , value, footnote 
# @adsh,@tag, @version, @coreg, @ddate , @qtrs  , @uom  , @value, @footnote 

#process num.txt.file
with open(numTxtFile, newline='', encoding='latin-1') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    columns = next(reader) 

    for line in reader:
        cursor = connection.cursor()
        for data in reader:
            print (data)
            (adsh,tag, version, coreg, ddate , qtrs  , uom  , value, footnote ) = data
            params = (adsh,tag, version, coreg, ddate , qtrs  , uom  , value, footnote )
            cursor.execute("{CALL dbo.[InsertFactsNumeric] (?,?,?,?,?,?,?,?,?)}", params)
        cursor.commit()
connection.close()
 
