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
        self.assertTrue(receiver.formulateReadings("5,10,20\n6,15,30") == [[5,10,20],[6,15,30]])

    def test_extractEachParameterReadings(self):
        self.assertTrue(receiver.extractEachParameterReadings([[5,10,20],[6,15,30]], "soc") == [5,6])
        self.assertTrue(receiver.extractEachParameterReadings([[5,10,20],[6,15,30]], "temp") == [10,15])
        self.assertTrue(receiver.extractEachParameterReadings([[5,10,20],[6,15,30]], "chargeRate") == [20,30])

if __name__ == '__main__': # pragma: no cover
  unittest.main()