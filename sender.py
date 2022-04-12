import json
import csv
import sys

def sendSensorData(fileName, readReadingsFromCSV, formatOutputString, printOnConsole):
    readings = readReadingsFromCSV(fileName)
    for reading in readings:
        formattedstring = formatOutputString(reading)
        sys.stdout.flush()
        printOnConsole(formattedstring)
    return True

def readReadingsFromCSV(fileName):
    list = []
    readingCount = 1
    with open(fileName) as file:
        for i in csv.DictReader(file):
            list.append(dict(i))
            readingCount =+ 1
        return list

def formatOutputStringAsJSON(streamReading):
    json_object = json.dumps(streamReading, indent = 4)
    return json_object

def formatOutputStringAsCSV(streamReading):
    return f'{streamReading["soc"]},{streamReading["temp"]},{streamReading["chargeRate"]}'

def printOnConsole(string):
    print(string)
    return True

if __name__ == '__main__': # pragma: no cover
  sendSensorData("./sensorData/Readings.csv", readReadingsFromCSV, formatOutputStringAsCSV, printOnConsole)