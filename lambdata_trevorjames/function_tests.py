"""
Tests for python modules
"""

import unittest
# testing two different functions in my package

from lambdata_trevorjames.things import Character, Wizard


class UnitTests(unittest.TestCase):
    def test_character(self):
        """Testing Character feilds are met"""
        x = Character('trevor', 200, 100)
        # assert character name = 'trevor'
        self.assertEqual(x.name, 'trevor')
        self.assertEqual(x.weight, 200)

    def test_weight(self):
        """testing if adding food works correctly"""
        x = Character('trevor', 200, 100)
        x.add_weight(10)
        self.assertEqual(x.weight, 210)

    def test_wizard(self):
        """testing wizard inherits Character Qualities"""
        x = Wizard('trevor', 200, 100, 'expeliamous')
        x.cast_spell()
        self.assertEqual(x.cast_spell(), 'Abrakadabra')



if __name__ == '__main__':
    unittest.main()
