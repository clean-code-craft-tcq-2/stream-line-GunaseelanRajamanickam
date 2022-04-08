import unittest
import sender

class SenderTest(unittest.TestCase):
    def test_printOnConsole(self):
        self.assertTrue(sender.printOnConsole('All is fine!') == True)

    def test_formatOutputStringAsCSV(self):
        self.assertTrue(sender.formatOutputStringAsCSV({'soc':25,'temp':30,'chargeRate':60}) == "25,30,60")

    def test_formatOutputStringAsJSON(self):
        expectedOutput = "{\n    \"soc\": 25,\n    \"temp\": 30,\n    \"chargeRate\": 60\n}"
        self.assertTrue(sender.formatOutputStringAsJSON({'soc':25,'temp':30,'chargeRate':60}) == expectedOutput)
    
    def test_readReadingsFromCSV(self):
        self.assertTrue(sender.readReadingsFromCSV("/sensorData/ReadingsTest.csv") == [{'soc': '20', 'temp': '30', 'chargeRate': '20'}, {'soc': '22', 'temp': '32', 'chargeRate': '25'}])

    def test_sendSensorData(self):
        self.assertTrue(sender.sendSensorData("/sensorData/ReadingsTest.csv", sender.readReadingsFromCSV, sender.formatOutputStringAsCSV, sender.printOnConsole) == True)
        self.assertTrue(sender.sendSensorData("/sensorData/ReadingsTest.csv", sender.readReadingsFromCSV, sender.formatOutputStringAsJSON, sender.printOnConsole) == True)

if __name__ == '__main__': # pragma: no cover
  unittest.main()