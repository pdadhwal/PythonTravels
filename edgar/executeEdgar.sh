#!/bin/bash

pidPRE=
pidNUM=
pidSUB=

forceDownload=F

function runPRE(){
	year=$1
	quarter=$2
	echo "run PRE $year $quarter"
	python ProcessPREdataFile.py $year $quarter &
	pidPRE=$!
	echo "PRE PID $pidPRE"
}

function runNUM() {
	year=$1
	quarter=$2
	echo "run NUM $year $quarter"
	python ProcessNUMericDataFile.py $year $quarter &
	pidNUM=$!
	echo "NUM PID $pidNUM"
}

function runSUB(){
	year=$1
	quarter=$2
	echo "run SUB $year $quarter"
	python ProcessEdgarSUBdataFile.py $year $quarter &
	pidSUB=$!
	echo "SUB PID $pidSUB"
}

function runDownload {
	year=$1
	quarter=$2
	
	echo "run Download $year $quarter"
	if [ "xx$forceDownload" == "xxF" ]; then
		python DownloadProcessedZipFiles.py $year $quarter
	else
		echo "$year $quarter data will not be downloaded"
	fi
}

function runOneBatch {
	year=$1
	quarter=$2

	runDownload $year $quarter
	runNUM $year $quarter
	runSUB $year $quarter
	runPRE $year $quarter

	echo "Waiting for batch $year $quarter to finish..."
	wait
	echo "Done!"
}

function runAll() {
	years="2018 2017 2016 2015 2014 2013 2012 2011 2010 2009"
	quarters="q1 q2 q3 q4"

	for year in $years;
	do
		for quarter in $quarters;
		do
			runOneBatch $year $quarter
		done
		
	done
}

if [ $# == 0 ]; then
	runAll
else
	runOneBatch $1 $2
fi

