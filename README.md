# Streaming BMS Data

This project is about sending and receiving BMS data.

## Decomposition

At a top level, the program runs in two processes - the sender and the receiver.

```mermaid
flowchart LR
A((sensor1)) --> Sender
B((sensor2)) --> Sender
Sender --> |line-by-line-via-console|Receiver
Receiver --> |statistics|C((Output))
```

The Sender simulates and processes data from sensors. It sends data line-by-line to the console, in a format that it defines.
The Receiver inputs this data and computes statistics.

The Sender sends data to the Receiver using [console redirection and pipes](https://ss64.com/nt/syntax-redirection.html).
They need to run on the command-line as follows:

`sender-executable | receiver-executable`

This would make the console-writes of the sender
become the console-reads of the receiver.
It gives us the flexibility of decoupling the sender and receiver -
they can even be written in different languages.

## Phases

The project is divided into two phases:

- Develop the Sender in the first phase, complete with test cases. The syntax and meaning of the data must be evident by reading your test cases.
Do not develop the Receiver yet.

We will instruct you to handover your Sender to another participant and take-over another Sender.

- Develop the Receiver for the Sender you take-over.

## The Interface

We document the interface between the Sender and the Receiver as test cases.

The Sender and Receiver are testable on their own:

- The Sender is testable without the Receiver - so we can develop
for another sensor, test and be confident about integration.
- The Receiver is testable without the Sender - so we can enhance
without re-testing against all Receivers again.

## Decomposition of responsibility

The naming of source files within the Sender and within the Receiver
give their internal decomposition.

## Minimum Functionality

This section lists the minimum functionality of the Sender and Receiver.

### The Sender

- simulates and sends at least two Battery / Charging parameters
- sends fifty readings in a stream
- can either generate values for the parameters, or read from a file
- uses console output to communicate the parameters.

# Test Specification for the Sender
### 1. Create a simple `sendSensorData` with a method:
```
sendSensorData(fileName)
```
The method reads the sensor data from the csv file which is supported by method `readReadingsFromCSV` which convert the csv into a dict
### 2. Support `sendSensorData` to format the readings of dict into csv format
### 3. Support `sendSensorData` to format the readings of dict into JSON format
### 4. Support `sendSensorData` to print the formatted string in console
### The Receiver

- reads the parameters from the console input
- after reading every parameter, it prints the following:
    - maximum and minimum values in the incoming stream
    - [simple moving average](https://www.investopedia.com/terms/s/sma.asp) of the last 5 values

# Test Specification for the Receiver
### 1. Create a simple Min and Max of array of readings with a method:
```
calculateMinMaxReading(readings)
```
The method can take an array and return the dict of min and max of array using the following methods.
```
calculateMinReading(readings)
calculateMaxReading(readings)
```

### 2. Create a simple moving average calculator for readings of window size 5 with a method:
```
calculateMovingAverage(readings, windowSize)
```
The method can take an array and return the simple moving average using the following methods.
```
createWindow(readings, windowSize)
calculateSum(array)
calculateAverage(array)
roundOffAverage(value, digits)
```
### 3. Create a simple `inferReceivedData` method to integrate `calculateMinMaxReading` and `calculateMovingAverage`.
### 4. Support `inferReceivedData` method to convert the statistics in csv format:
For example, `soc:{'min': 20.0, 'max': 31.0},[23.8, 25.4, 26.8, 28.2]`.
### 5. Support `inferReceivedData` method to print the formatted string in console
### 6. Allow `inferReceivedData` method to handle multiple parameter readings
For example, `soc`, `temp`, `chargeRate`
### 7. Allow `inferReceivedData` method to read the console output of `sender.py`

## Quality Parameters

Setup the quality parameters of your project (duplication, complexity, coverage, warnings) using GitHub workflow yml files.
