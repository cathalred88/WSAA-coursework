## trains.py
# Author Cathal Redmond Date 4 Feb 2026
# this Lab is a n excercise to retrieve train timetables form Irish Rail API and perfrom some data anaylsis on the information retunred. 

# imports
import requests
import csv
from xml.dom.minidom import parseString

#create an array called retrieveTags that will store all the names of the tags we want to retrieve. 
retrieveTags = ['TrainStatus',
                'TrainLatitude',
                'TrainLongitude',
                'TrainCode',
                'TrainDate',
                'PublicMessage',
                'Direction'
                ]

# define variables
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
with open('week02_trains.csv', mode="w", newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter = "\t", quotechar = '"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)

#Check if it works
#print (doc.toprettyxml()) # this outputs the xml to the console . We can remove this once it works, or comment it out. 

# if we want to store the xml in a file - we can comment this out later also. 
with open("train.xml", "w") as xmlfp:
    doc.writexml(xmlfp)