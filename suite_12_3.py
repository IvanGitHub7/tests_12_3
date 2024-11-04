import unittest
import test_12_3

rtTest = unittest.TestSuite()


rtTest.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
rtTest.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(rtTest)

