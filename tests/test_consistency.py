import unittest
import re
import json

from flydenity import Parser


class TestParseConsistency(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_general_available_for_country(self):
        """Every country must have 'general' data."""

        is_broken = False
        countries = {}
        for datasets in self.parser.callsigns.values():
            for dataset in datasets:
                if dataset['type'] != 'country':
                    continue

                if dataset['iso2'] not in countries:
                    countries[dataset['iso2']] = [dataset['description']]
                else:
                    countries[dataset['iso2']].append(dataset['description'])

        for country, descriptions in countries.items():
            if 'general' not in descriptions:
                print(f"country '{country}' does not have 'general' data.")
                is_broken = True

        self.assertFalse(is_broken, "We have countries without 'general' data.")

    def test_suffix_pattern(self):
        """Every suffix must match with r'([A-Z0-9]+)(\-[A-Z0-9]+)?'."""

        is_broken = False
        for datasets in self.parser.callsigns.values():
            for dataset in datasets:
                for suffix in dataset['suffixes']:
                    if not re.match(r'^([A-Z0-9]+)(\-[A-Z0-9]+)?$', suffix):
                        print(f"dataset '{dataset}' has a bad suffix pattern: '{suffix}'")
                        is_broken = True

        self.assertFalse(is_broken, "We found bad suffixes.")

    def test_suffix_consistency(self):
        """A valid registration (callsign + suffix) must match with the given regex."""

        is_broken = False
        overlapping_datasets = set()
        for datasets in self.parser.callsigns.values():
            for dataset in datasets:
                registrations = []
                for callsign in dataset['callsigns']:
                    for suffix in dataset['suffixes']:
                        if re.match(r'^([A-Z0-9]+)(\-[A-Z0-9]+)?$', suffix) is None:
                            continue    # suffix is broken... already tested above

                        if '-' in suffix:
                            registrations.extend([f"{callsign}-{suffix}" for suffix in suffix.split('-')])
                        else:
                            registrations.append(f"{callsign}-{suffix}")

                # registration must fit with the regex
                for registration in registrations:
                    if re.match(dataset['regex'], registration) is None:
                        print(f"registration '{registration}' does not fit into regex '{dataset['regex']}'")
                        is_broken = True

                # check country dependant registrations ...
                if 'iso2' not in dataset:
                    continue

                # ... and find non unique matches
                for registration in registrations:
                    other_datasets = [other_dataset for other_dataset in self.parser._parse_registration(registration, strict=True) if other_dataset != dataset]
                    if len(other_datasets) > 1:
                        for other_dataset in other_datasets:
                            overlapping_datasets.add(json.dumps([self.parser._data_to_result(dataset), self.parser._data_to_result(other_dataset)]))
                            is_broken = True

        for overlapping in overlapping_datasets:
            dataset, other_dataset = json.loads(overlapping)
            print(f"overlapping matches found: {dataset} vs. {other_dataset}")

        self.assertFalse(is_broken, "We found bad suffixes not matching with the regex or not unique matches.")

    def test_icao24bit_registration(self):
        """ICAO 24bit registrations must match with on result only."""

        is_broken = False
        for i in range(0, int('FFFFFF', 16), 32):
            icao24bit = f"{i:06X}"
            matches = self.parser._parse_icao24bit(icao24bit, strict=True)
            if matches and len(matches) > 1:
                print(f"{icao24bit} -> {matches}")
                is_broken = True

        self.assertFalse(is_broken, "We found ICAO 24bit registrations with multiple matches")

if __name__ == '__main__':
    unittest.main()
