import io
import os
import csv
import sys

# TODO process this from the command line
year = sys.argv[1]
quarter = sys.argv[2]

# Download index files and write content into SQLite
import pypyodbc
connection = pypyodbc.connect('Driver={SQL Server};Server=PRAMENDRA-PC\SQLEXPRESS01;Database=edgar;Trusted_Connection=yes;')
cur = connection.cursor()
cur.execute("if not exists (select * from sysobjects where name='XBRLSubmissions' and xtype='U') CREATE TABLE XBRLSubmissions (adsh varchar(40), cik varchar(20), name varchar(300),sic varchar(8), countryba varchar(4),	stprba varchar(4),	cityba varchar(100), zipba varchar(20),bas1 varchar(80), bas2 varchar(80),baph varchar(24),countryma varchar(4), stprma varchar(4), cityma varchar(60), zipma varchar(20),	mas1 varchar(80),mas2 varchar(80),	countryinc varchar(25),	stprinc varchar(20),ein varchar(40),former varchar(300),changed varchar(16),afs varchar(10),wksi varchar(2),fye varchar(8),form varchar(20),period varchar(16),fy varchar(8),fp varchar(4),	filed varchar(16), accepted varchar(38),prevrpt varchar(2),detail varchar(2),	instance varchar(64),nciks varchar(8),	aciks varchar(240))")

outputDir = '%s%s' % (year , quarter)

# numTxtFile = '.\%s\\num.txt' % (outputDir)
#    preTxtFile = '.\%s\\pre.txt' % (outputDir)
subTxtFile = '.\%s\\sub.txt' % (outputDir)
#    tagTxtFile = '.\%s\\tag.txt' % (outputDir)

print(outputDir)
print(subTxtFile)

# TODO: Exit with error if the num.txt file does not exist

#process num.txt.file
with open(subTxtFile , newline='', encoding='latin-1') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    columns = next(reader) 
    print(','.join(columns))
    
    # precreate table
    # adsh varchar(200)
	# cik varchar(200)
	# name varchar(200)
	# sic varchar(200)
    # countryba varchar(200)
	# stprba varchar(200),	
	# cityba varchar(200), 
	# zipba varchar(200),
	# bas1 varchar(200),
	# bas2 varchar(200),
	# baph varchar(200),
	# countryma varchar(200), 
	# stprma varchar(200), 
	# cityma varchar(200), 
	# zipma varchar(200),	
	# mas1 varchar(200),
	# mas2 varchar(200),	
	# countryinc varchar(200),	
	# stprinc varchar(200),
	# ein varchar(200),
	# former varchar(200),
	# changed varchar(200),
	# afs varchar(200),
	# wksi varchar(200),
	# fye varchar(200),
	# form varchar(200),
	# period varchar(200),
	# fy varchar(200),
	# fp varchar(200),	
	# filed varchar(200), 
	# accepted varchar(200),
	# prevrpt varchar(200),
	# detail varchar(200),	
	# instance varchar(200),
	# nciks varchar(200),	
	# aciks varchar(200),
	# pubfloatusd varchar(200),
	# floatdate varchar(200),
    for line in reader:
        cursor = connection.cursor()
        for data in reader:
            print (data)
            (adsh,cik,name,sic,countryba,stprba,cityba,zipba,bas1,bas2,baph,countryma,stprma,cityma,zipma,mas1,mas2,countryinc,stprinc,ein,former,changed,afs,wksi,fye,form,period,fy,fp,filed,accepted,prevrpt,detail,instance,nciks,aciks,pubfloatusd,floatusd) = data
            params = (adsh,cik,name,sic,countryba,stprba,cityba,zipba,bas1,bas2,baph,countryma,stprma,cityma,zipma,mas1,mas2,countryinc,stprinc,ein,former,changed,afs,wksi,fye,form,period,fy,fp,filed,accepted,prevrpt,detail,instance,nciks,aciks)
            cursor.execute("{CALL dbo.InsertSubmissions (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)}", params)
        cursor.commit()
connection.close()
 
