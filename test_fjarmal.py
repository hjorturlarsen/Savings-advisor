import unittest
import math

# Here's our "unit".
import reiknivelar

# Here's our "unit tests".
class TestsClass(unittest.TestCase):

    def testOne_framtidarvirdi(self):
        self.failUnlessAlmostEqual(reiknivelar.framtidarvirdi(100000, 10, 12), 310584.8, places = 1)
    def testTwo_framtidarvirdi(self):
        self.failUnlessAlmostEqual(reiknivelar.framtidarvirdi(240000, 13, 45), 30060435.7, places = 1 )

    def testOne_reglulegurspar(self):
        self.failUnlessAlmostEqual(reiknivelar.reglulegurspar(9500, 12, 31), 131676.81, places = 1)
    def testTwo_reglulegurspar(self):
        self.failUnlessAlmostEqual(reiknivelar.reglulegurspar(95000,24,2), 2324238.8, places = 1)

    def testOne_sparnadar_takmark(self):
        self.failUnlessAlmostEqual(reiknivelar.sparnadar_takmark(100000, 2000, 24, 13), 28.0, places = 1)
    def testTwo_sparnadar_takmark(self):
        self.failUnlessAlmostEqual(reiknivelar.sparnadar_takmark(1000, 2, 23, 22), 0.0, places = 1)

    def testOne_sparnadar_timi(self):
        self.failUnlessAlmostEqual(reiknivelar.sparnadar_timi(100000, 520, 3), (13, 2.0), places = 1)
    def testTwo_sparnadar_timi(self):
        self.failUnlessAlmostEqual(reiknivelar.sparnadar_timi(100000000, 1000, 34), (23, 9.0), places = 1)

    def testOne_sparnadur_a_manudi(self):
        self.failUnlessAlmostEqual(reiknivelar.sparnadur_a_manudi(15000, 20, 3), 287.5, places = 1)
    def testTwo_sparnadur_a_manudi(self):
        self.failUnlessAlmostEqual(reiknivelar.sparnadur_a_manudi(152000, 2, 7), 1140.0, places = 1)

    def testOne_manadarlegar_greidslur_af_lani(self):
        self.failUnlessAlmostEqual(reiknivelar.manadarlegar_greidslur_af_lani(10000000, 240), 41666.66666, places = 1)
    def testTwo_manadarlegar_greidslur_af_lani(self):
        self.failUnlessAlmostEqual(reiknivelar.manadarlegar_greidslur_af_lani(95000000, 7000), 13571.4, places = 1)

def main():
    unittest.main(verbosity = 18, exit = False)

if __name__ == '__main__':
    main()