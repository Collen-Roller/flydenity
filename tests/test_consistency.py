import unittest
import os
import re

from flydenity.parser import ARParser


class TestParse(unittest.TestCase):
    def setUp(self):
        self.parser = ARParser()

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
        overlappings = set()
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

                # registration should no be valid for other countries
                if 'iso2' not in dataset:
                    continue

                
                for registration in registrations:
                    for other_dataset in self.parser.parse(registration):
                        if 'iso2' in other_dataset and other_dataset['iso2'] != dataset['iso2']:
                            overlappings.add(str(sorted((dataset['iso2'], other_dataset['iso2']))))
                            is_broken = True
        
        for overlapping in overlappings:
            (iso2_1, iso2_2) = overlapping[1:-1].split(', ')
            print(f"overlapping found: {iso2_1} vs. {iso2_2}")

        self.assertFalse(is_broken, "We found bad suffixes not matching with the regex or not unique in iso2.")
