import unittest

from flydenity import Parser

class TestParse(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_parse_simple(self):
        match = self.parser.parse('D-1234')

        self.assertEqual(match, {'nation': 'Germany', 'description': 'gliders', 'iso2': 'DE', 'iso3': 'DEU'})

    def test_parse_icao(self):
        match = self.parser.parse('4Y-AAA')

        self.assertEqual(match, {'name': 'International Civil Aviation Organization', 'description': 'general'})

    def test_parse_tahiti(self):
        match = self.parser.parse('F-OHJJ')

        self.assertEqual(match, {'nation': 'Tahiti or French Polynesia', 'description': 'general', 'iso2': 'PF', 'iso3': 'PYF'})

    def test_parse_strict(self):
        sloppy_reg_sloppy_parser = self.parser.parse('D0815', strict=False)
        sloppy_reg_strict_parser = self.parser.parse('D0815', strict=True)
        strict_reg_sloppy_parser = self.parser.parse('D-0815', strict=False)
        strict_reg_strict_parser = self.parser.parse('D-0815', strict=True)

        self.assertTrue(sloppy_reg_sloppy_parser == strict_reg_sloppy_parser == strict_reg_strict_parser != sloppy_reg_strict_parser)

    def test_parse_invalid(self):
        match = self.parser.parse('Hello there')

        self.assertIsNone(match)


if __name__ == '__main__':
    unittest.main()
