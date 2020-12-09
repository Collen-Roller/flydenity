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


class ARParser():
    def __init__(self):
        # read the input files into the callsign mapping: callsign -> [data1, data2, ...]
        self.callsigns = {}
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
                    data['callsigns'] = [callsign[1:-1] for callsign in raw_data['callsign'][1:-1].split(', ')]
                    data['suffixes'] = [suffix[1:-1] for suffix in raw_data['suffix'][1:-1].split(', ')]
                    data['regex'] = re.compile(raw_data['regex'])

                    strict_regex = raw_data['regex'].replace('-{0,1}', '\-').replace('{0,1}$', '$')
                    data['strict_regex'] = re.compile(strict_regex)

                    for callsign in data['callsigns']:
                        if callsign not in self.callsigns:
                            self.callsigns[callsign] = [data]
                        else:
                            self.callsigns[callsign].append(data)

        self.min_callsign_len = min([len(callsign) for callsign in self.callsigns.keys()])
        self.max_callsign_len = max([len(callsign) for callsign in self.callsigns.keys()])

    def parse(self, string, strict=False):
        # find the datasets matching with the string
        datasets = []
        for callsign_len in range(self.min_callsign_len, self.max_callsign_len+1):
            if string[0:callsign_len] in self.callsigns.keys():
                datasets.extend(self.callsigns[string[0:callsign_len]])

        # return None if no dataset found
        if datasets == []:
            return None

        # match the string with the datasets
        country_matches = []
        organization_matches = []
        for data in datasets:
            match = data['strict_regex'].match(string) if strict is True else data['regex'].match(string)
            if match:
                if data['type'] == 'country':
                    country_matches.append({
                        'nation': data['nation'],
                        'description': data['description'],
                        'iso2': data['iso2'],
                        'iso3': data['iso3']
                    })
                elif data['type'] == 'organization':
                    organization_matches.append({
                        'name': data['name'],
                        'description': data['description']
                    })

        # return matches we found
        if len(country_matches) > 0 or len(organization_matches) > 0:
            return country_matches + organization_matches

        # return None if the string doesn't match with any of the datasets
        else:
            return None
