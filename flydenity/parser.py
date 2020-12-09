"""

parser.py
Collen Roller
collen.roller@gmail.com

Main parser for Regexs that exist within the dataset
"""

import pandas as pd
import ast
import os
import re
import sys

class ARParser():


    dataset_files = {"countries":os.path.join(os.path.dirname(__file__),
                     "processed_itu_countries_regex.csv"),
                     "organizations":os.path.join(os.path.dirname(__file__),
                     "processed_itu_organizations_regex.csv")}

    def __init__(self):
        self.datasets_loaded = False
        self.load_datasets(self.dataset_files)

    def load_datasets(self, files):
        try:
            if files is not None:
                self.dfs = {}
                for key, f in files.items():
                    self.dfs[key] = pd.read_csv(f)
                self.datasets_loaded = True
            else:
                self.print_dataset_error()
        except:
            self.print_dataset_error()

    def parse(self, callsign):
        res = []
        if not self.datasets_loaded:
            self.load_datasets(self.dataset_files)
        else:
            #parse the data
            for key, df in self.dfs.items():
                for index, entry in df.iterrows():
                    result = re.match(entry['regex'], callsign)
                    if result is not None:
                        #print("Success!")
                        #print(entry)
                        codes = ast.literal_eval(entry["iso codes"])
                        print(codes)
                        res.append({"nation":entry["nation"],
                                    "description":entry["description"],
                                    "iso codes":codes})

        return res

    def print_dataset_error(self):
        print("Can't identify dataset, try loading it manually")
        print("Use load_dataset(<tags.csv>)")
