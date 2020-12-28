"""

parser.py
Collen Roller
collen.roller@gmail.com

Main parser for Regexs that exist within the dataset
"""

import os
import re
import csv


CURRENT_PATH = os.path.dirname(__file__)
DATASET_FILES = {
    "countries": "processed_itu_countries_regex.csv",
    "organizations": "processed_itu_organizations_regex.csv"
}


class Parser():
    def __init__(self):
        # read the input files into mappings:
        self.callsigns = {}     # the callsign mapping: callsign -> [data1, data2, ...]
        self.icao24bit = {}     # the icao24bit mapping: icao24bit_prefix -> data
        for dataset_type in DATASET_FILES:
            with open(os.path.join(CURRENT_PATH, DATASET_FILES[dataset_type])) as csvfile:
                csvreader = csv.reader(csvfile)
                header = next(csvreader)
                for row in csvreader:
                    raw_data = {key: value for (key, value) in zip(header, row)}

                    data = {}
                    if 'nation' in raw_data:
                        data['type'] = 'country'
                        data['nation'] = raw_data['nation']
                        iso_codes = [iso[1:-1] for iso in raw_data['iso codes'][1:-1].split(', ')]
                        data['iso2'] = iso_codes[0]
                        data['iso3'] = iso_codes[1]
                    elif 'name' in raw_data:
                        data['type'] = 'organization'
                        data['name'] = raw_data['name']
                    else:
                        raise ValueError(f"Input file for {dataset_type} '{DATASET_FILES[dataset_type]}' is corrupt.")

                    data['description'] = raw_data['description']
                    data['priority'] = raw_data['priority']
                    data['callsigns'] = [callsign[1:-1] for callsign in raw_data['callsign'][1:-1].split(', ')]
                    data['suffixes'] = [suffix[1:-1] for suffix in raw_data['suffix'][1:-1].split(', ')]
                    data['regex'] = re.compile(raw_data['regex'])
                    data['icao24bit_from'] = raw_data['icao24bit_from']
                    data['icao24bit_to'] = raw_data['icao24bit_to']
                    data['icao24bit_prefixes'] = [prefix[1:-1] for prefix in raw_data['icao24bit_prefix'][1:-1].split(', ')] if len(raw_data['icao24bit_prefix']) > 0 else []

                    strict_regex = raw_data['regex'].replace('-{0,1}', '\-').replace('{0,1}$', '$')
                    data['strict_regex'] = re.compile(strict_regex)

                    for callsign in data['callsigns']:
                        if callsign not in self.callsigns:
                            self.callsigns[callsign] = [data]
                        else:
                            self.callsigns[callsign].append(data)

                    for prefix in data['icao24bit_prefixes']:
                        self.icao24bit[prefix] = data

        self.min_callsign_len = min([len(callsign) for callsign in self.callsigns.keys()])
        self.max_callsign_len = max([len(callsign) for callsign in self.callsigns.keys()])

    def _data_to_result(self, data):
        if data['type'] == 'country':
            return {
                'nation': data['nation'],
                'description': data['description'],
                'iso2': data['iso2'],
                'iso3': data['iso3']
            }
        elif data['type'] == 'organization':
            return {
                'name': data['name'],
                'description': data['description']
            }

    def _parse_registration(self, string, strict):
        # find the datasets matching with the string
        datasets = []
        for callsign_len in range(self.min_callsign_len, self.max_callsign_len+1):
            if string[0:callsign_len] in self.callsigns.keys():
                datasets.extend(self.callsigns[string[0:callsign_len]])

        # return None if no dataset found
        if datasets == []:
            return None

        # match the string with the datasets
        matches_by_priority = {}
        for data in datasets:
            match = data['strict_regex'].match(string) if strict is True else data['regex'].match(string)
            if match:
                if data['priority'] not in matches_by_priority:
                    matches_by_priority[data['priority']] = [data]
                else:
                    matches_by_priority[data['priority']].append(data)

        # from all matches we found return the match(es) with the highest priority
        if len(matches_by_priority) > 0:
            best_matches = matches_by_priority[max(matches_by_priority.keys())]
            return best_matches

        # return None if the string doesn't match with any of the datasets
        else:
            return None

    def _parse_icao24bit(self, string, strict):
        # check if input is correct
        if strict and not re.match('[0-9A-F]{6}', string):
            print(f"Warning: ICAO 24bit must be hexadecimal with length of 6 chars")
            return None

        # return the matches
        matches = []
        for prefix in [string[0:i+1] for i in range(len(string))]:
            if prefix in self.icao24bit:
                matches.append(self.icao24bit[prefix])

        return matches if len(matches) > 0 else None

    def parse(self, string, strict=False, icao24bit=False):
        if icao24bit is False:
            matches = self._parse_registration(string, strict)
            if matches:
                return self._data_to_result(matches[0])
        else:
            matches = self._parse_icao24bit(string, strict)
            if matches:
                return self._data_to_result(matches[0])
