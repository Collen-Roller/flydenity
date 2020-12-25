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

    def test_icao24bit_consistency(self):
        """ICAO 24bit registrations must match with on result only."""

        is_broken = False
        for i in range(0, int('FFFFFF', 16), 32):
            icao24bit = f"{i:06X}"
            print(icao24bit)
            matches = self.parser._parse_icao24bit(icao24bit, strict=True)
            if matches and len(matches) > 1:
                print(f"{icao24bit} -> {matches}")
                is_broken = True

        self.assertFalse(is_broken, "We found ICAO 24bit registrations with multiple matches")


if __name__ == '__main__':
    unittest.main()
