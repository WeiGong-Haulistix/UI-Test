import unittest
from Testcases.test_Cases import *


if __name__ == "__main__":
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestExecute)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(TestProcess)
    # suite3 = unittest.TestLoader().loadTestsFromTestCase(TestEditProcess)
    # suite = unittest.TestSuite([suite1, suite2, suite3])
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)
