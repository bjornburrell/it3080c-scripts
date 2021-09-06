#!/bin/bash
# This script will query covid data and display it
DATA=$(curl https://api.covidtracking.com/v1/us/current.json)

POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalizedCurrently')
TODAY=$(date)

echo " On $TODAY, there were $POSITIVE positive covid cases... $NEGATIVE nehgative cases... $HOSPITALIZED are currently hospitalized.... GET VAXXED YO"
