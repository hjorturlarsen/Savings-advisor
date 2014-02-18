import unittest
import math

# Here's our "unit".
import reiknivelar

# Here's our "unit tests".
class TestsClass(unittest.TestCase):

    def testOne_framtidarvirdi(self):
        self.failUnless(reiknivelar.framtidarvirdi(999584652, 26, 354))
    def testTwo_framtidarvirdi(self):
        self.failIf(reiknivelar.framtidarvirdi(10010.123, 9999999999999, 3223))

    def testOne_reglulegurspar(self):
        self.failUnless(reiknivelar.reglulegurspar(10012000, 22.2, 3123))
    def testTwo_reglulegurspar(self):
        self.failUnless(reiknivelar.reglulegurspar(13000, 24, 32))
    def testThree_reglulegurspar(self):
        self.failUnless(reiknivelar.reglulegurspar(1000, 2, 3523))

    def testOne_sparnadar_takmark(self):
        self.failUnless(reiknivelar.sparnadar_takmark(99999987, 500, 24, 13))
    def testTwo_sparnadar_takmark(self):
        self.failUnless(reiknivelar.sparnadar_takmark(102200, 50.20, 2.0003, 32))
    def testThree_sparnadar_takmark(self):
        self.failUnless(reiknivelar.sparnadar_takmark(1000, 500, 2, 3))

    def testOne_sparnadar_timi(self):
        self.failUnless(reiknivelar.sparnadar_timi(10001123, 520, 2.0234))
    def testTwo_sparnadar_timi(self):
        self.failUnless(reiknivelar.sparnadar_timi(1099300, 50.23, 20))
    def testThree_sparnadar_timi(self):
        self.failUnless(reiknivelar.sparnadar_timi(91000, 50, 2000))

    def testOne_sparnadur_a_manudi(self):
        self.failUnless(reiknivelar.sparnadar_timi(99999991000, 50, 245))
    def testTwo_sparnadur_a_manudi(self):
        self.failUnless(reiknivelar.sparnadar_timi(1000, 50, 2))
    def testThree_sparnadur_a_manudi(self):
        self.failUnless(reiknivelar.sparnadar_timi(100.2340, 50.123, 2000))

    def testOne_manadarlegar_greidslur_af_lani(self):
        self.failUnless(reiknivelar.sparnadar_timi(902391000, 50, 2))
    def testTwo_manadarlegar_greidslur_af_lani(self):
        self.failUnless(reiknivelar.sparnadar_timi(100023, 50, 2.455432))
    def testThree_manadarlegar_greidslur_af_lani(self):
        self.failUnless(reiknivelar.sparnadar_timi(1000, 50, 2))

def main():
    unittest.main(verbosity = 18, exit = False)

if __name__ == '__main__':
    main()