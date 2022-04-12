
import sys

parameters = ["soc", "temp", "chargeRate"]

def inferReceivedData(windowSize, readFromConsole, formulateReadings, extractEachParameterReadings, calculateMovingAverage, calculateMinMaxReading, convertCSVFormat, printOnConsole):
    stream = readFromConsole()
    mergedreadings = formulateReadings(stream)
    for parameter in parameters:
        readings = extractEachParameterReadings(mergedreadings, parameter)
        movingAverage = calculateMovingAverage(readings, windowSize)
        minMaxReading = calculateMinMaxReading(readings)
        formattedString = convertCSVFormat(parameter,minMaxReading,movingAverage)
        printOnConsole(formattedString)

def readFromConsole():
    print(sys.version)
    lines = sys.stdin.readlines()
    return lines
    
def formulateReadings(stream):
    mergedReadings = []
    for csvReading in stream:
        csvReading = csvReading.strip('\n')
        reading = list(map(float,csvReading.split(',')))
        mergedReadings.append(reading)
    return mergedReadings

def extractEachParameterReadings(mergedReadings, parameter):
    index = getindex(parameter)
    return [readings[index] for readings in mergedReadings]

def getindex(parameter):
    for index, parameterName in enumerate(parameters):
        if parameterName == parameter:
            return index

def calculateMovingAverage(readings, windowSize):
    windows = createWindow(readings, windowSize)
    movingAverages = [roundOffAverage(calculateAverage(window), 2) for window in windows]
    return movingAverages

def roundOffAverage(value, digits):
    return round(value, digits)

def calculateAverage(array):
    return calculateSum(array) / len(array)

def calculateSum(array):
    return sum(array)

def createWindow(readings, windowSize):
    windows = [readings[index : index + windowSize] for index, value in enumerate(readings) if index < len(readings) - windowSize + 1]
    return windows

def calculateMinMaxReading(readings):
    minReading = calculateMinReading(readings)
    maxReading = calculateMaxReading(readings)
    return {'min': minReading, 'max': maxReading}

def calculateMinReading(readings):
    return min(readings)

def calculateMaxReading(readings):
    return max(readings)

def convertCSVFormat(parameter,minMaxReading,movingAverage):
  return f'{parameter}:{minMaxReading},{movingAverage}'

def printOnConsole(string):
    print(string)
    return True

if __name__ == '__main__':  # pragma: no cover
  inferReceivedData(5, readFromConsole, formulateReadings, extractEachParameterReadings, calculateMovingAverage, calculateMinMaxReading, convertCSVFormat, printOnConsole)