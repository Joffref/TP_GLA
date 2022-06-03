import unittest
from exo2 import *

class Test_Exo2(unittest.TestCase):
    
    def test_freinage_v_is_0(self):
        self.assertEqual(freinage(0, False), 0)
    
    def test_freinage_v_is_30(self):
        self.assertEqual(freinage(30, False), 4)
    
    def test_freinage_v_is_30_wet(self):
        self.assertEqual(freinage(30, True), 9)
    
    def test_reaction_v_is_0(self):
        self.assertEqual(reaction(0), 0)
    
    def test_reaction_v_is_30(self):
        self.assertEqual(reaction(30), 8)
    
    def test_distanceDarret_v_is_0(self):
        self.assertEqual(distanceDarret(0, False), 0)
    
    def test_distanceDarret_v_is_30(self):
        self.assertEqual(distanceDarret(30, False), 12)
    
    def test_distanceDarret_v_is_30_wet(self):
        self.assertEqual(distanceDarret(30, True), 17)
    
    def test_verifierSiPossibleDeSarreter_v_is_0_d_is_1(self):
        self.assertEqual(verifierSiPossibleDeSarreter(0, 1, False), True)
    
    def test_verifierSiPossibleDeSarreter_v_is_30_d_is_1(self):
        self.assertEqual(verifierSiPossibleDeSarreter(30, 1, False), False)
    
    def test_verifierSiPossibleDeSarreter_v_is_30_wet_d_is_1(self):
        self.assertEqual(verifierSiPossibleDeSarreter(30, 1, True), False)
    
    def test_verifierSiPossibleDeSarreter_v_is_30_wet_d_is_60(self):
        self.assertEqual(verifierSiPossibleDeSarreter(30, 60, True), True)
    
    def test_freinage_result_is_type_int(self):
        self.assertEqual(type(freinage(30, False)), int)
    
    def test_reaction_result_is_type_int(self):
        self.assertEqual(type(reaction(30)), int)

if __name__ == '__main__':
    unittest.main()
