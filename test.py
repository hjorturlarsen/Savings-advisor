import unittest
import math
import reiknivelar
# Here's our "unit".

# Here's our "unit tests".
class TestsClass(unittest.TestCase):

    def testOne_framtidarvirdi(self):
        self.failUnless(reiknivelar.framtidarvirdi(1000, 2, 3))

    def testOne_reglulegurspar(self):
        self.failUnless(reiknivelar.reglulegurspar(1000, 2, 3))

    def testOne_sparnadar_takmark(self):
        self.failUnless(reiknivelar.sparnadar_takmark(1000, 500, 2, 3))

    def testOne_sparnadar_timi(self):
        self.failUnless(reiknivelar.sparnadar_timi(1000, 50, 2))

def main():
    unittest.main(verbosity = 4, exit = False)

if __name__ == '__main__':
    main()