from unittest import mock
import unittest
import receiver

class SenderTest(unittest.TestCase):
    def test_printOnConsole(self):
        self.assertTrue(receiver.printOnConsole('All is fine!') == True)
    
    def test_calculateMinMaxParameter(self):
        self.assertTrue(receiver.calculateMinMaxReading([5,10,2,3,10]) == {'min': 2, 'max': 10})
    
    def test_calculateMovingAverage(self):
        self.assertTrue(receiver.calculateMovingAverage([5,10,2,3,10,17,16,14], 5) == [6.0,8.4,9.6,12])
    
    def test_createWindow(self):
        self.assertTrue(receiver.createWindow([5,10,2,3,10,17,16,14], 5) == [[5, 10, 2, 3, 10], [10, 2, 3, 10, 17], [2, 3, 10, 17, 16], [3, 10, 17, 16, 14]])
    
    def test_formulateReadings(self):
        self.assertTrue(receiver.formulateReadings(['5,10,20\n','6,15,30\n']) == [[5,10,20],[6,15,30]])

    def test_extractEachParameterReadings(self):
        self.assertTrue(receiver.extractEachParameterReadings([[5,10,20],[6,15,30]], "soc") == [5,6])
        self.assertTrue(receiver.extractEachParameterReadings([[5,10,20],[6,15,30]], "temp") == [10,15])
        self.assertTrue(receiver.extractEachParameterReadings([[5,10,20],[6,15,30]], "chargeRate") == [20,30])

    @mock.patch('receiver.readFromConsole', return_value=['20,30,20\n', '22,32,25\n', '24,32,27\n', '26,32,28\n', '27,32,29\n', '28,32,30\n', '29,32,31\n', '31,33,32\n'])
    def test_inferReceivedData(self, mock_readFromConsole):
        expected_output = ["soc:{'min': 20.0, 'max': 31.0},[23.8, 25.4, 26.8, 28.2]", "temp:{'min': 30.0, 'max': 33.0},[31.6, 32.0, 32.0, 32.2]", "chargeRate:{'min': 20.0, 'max': 32.0},[25.8, 27.8, 29.0, 30.0]"]
        self.assertTrue(receiver.inferReceivedData(5, mock_readFromConsole, receiver.formulateReadings, receiver.extractEachParameterReadings, receiver.calculateMovingAverage, receiver.calculateMinMaxReading, receiver.convertCSVFormat, receiver.printOnConsole) == expected_output)

if __name__ == '__main__': # pragma: no cover
  unittest.main()