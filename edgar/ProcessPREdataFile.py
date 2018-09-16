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
cur.execute("if not exists (select * from sysobjects where name='XBRLPresentationOfStatements' and xtype='U') CREATE TABLE XBRLPresentationOfStatements (adsh varchar(40),report varchar(12),line varchar(12),stmt varchar(4),inpth varchar(2),rfile varchar(2),tag varchar(512),version varchar(40),plabel varchar(1024),negating varchar(2))")

outputDir = '%s%s' % (year , quarter)

# numTxtFile = '.\%s\\num.txt' % (outputDir)
preTxtFile = '.\%s\\pre.txt' % (outputDir)
# subTxtFile = '.\%s\\sub.txt' % (outputDir)
#    tagTxtFile = '.\%s\\tag.txt' % (outputDir)

print(outputDir)
print(preTxtFile)

# TODO: Exit with error if the num.txt file does not exist

#process num.txt.file
with open(preTxtFile , newline='', encoding='latin-1') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    columns = next(reader) 
    print(','.join(columns))
    
    # precreate table
    # adsh varchar(200),report varchar(200),line varchar(200),stmt varchar(200),inpth varchar(200),rfile varchar(200),tag varchar(500),version varchar(200),plabel varchar(1000),negating varchar(1)
    # @adsh ,@report ,@line,@stmt,@inpth,@rfile,@tag,@version,@plabel,@negating
    lineNumber = 1
    queryData=[]
    for line in reader:
        cursor = connection.cursor()
        for data in reader:
            (adsh ,report ,line,stmt,inpth,rfile,tag,version,plabel,negating ) = data
            queryData.append((adsh ,report ,line,stmt,inpth,rfile,tag,version,plabel,negating ))
		
        while len(queryData) !=0:
            cursor.executemany("{CALL dbo.[InsertPresentationOfStatements] (?,?,?,?,?,?,?,?,?,?)}", queryData[:999])
            del queryData[:999]
            lineNumber += 1
            print ('%s records committed' % (lineNumber))
        cursor.commit()
connection.close()
 
