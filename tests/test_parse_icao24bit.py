import unittest

from flydenity.parser import ARParser


class TestParse(unittest.TestCase):
    def setUp(self):
        self.parser = ARParser()

    def test_parse_simple(self):
        match = self.parser.parse('3D2591', icao24bit=True)

        self.assertEqual(match, {'nation': 'Germany', 'description': 'general', 'iso2': 'DE', 'iso3': 'DEU'})

    def test_parse_strict(self):
        sloppy_reg_sloppy_parser = self.parser.parse('3DX', icao24bit=True, strict=False)
        sloppy_reg_strict_parser = self.parser.parse('3DX', icao24bit=True, strict=True)
        strict_reg_sloppy_parser = self.parser.parse('3D2591', icao24bit=True, strict=False)
        strict_reg_strict_parser = self.parser.parse('3D2591', icao24bit=True, strict=True)

        self.assertTrue(sloppy_reg_sloppy_parser == strict_reg_sloppy_parser == strict_reg_strict_parser != sloppy_reg_strict_parser)


if __name__ == '__main__':
    unittest.main()
