<p align="center">
  <img src="/images/Box.png" width="350" title="ARP">
</p>

# <div align="center">Flydenity<br /><br />

[![PyPI version](https://badge.fury.io/py/flydenity.svg)](https://badge.fury.io/py/flydenity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/flydenity/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/flydenity/)
[![PyPI download month](https://img.shields.io/pypi/dm/ansicolortags.svg)](https://pypi.python.org/pypi/flydenity/)


# Flydenity - Aircraft Identification Library

Flydenity is a callsign identification library to help match tail numbers or
callsigns to origin nations. The library is a python wrapper on top of a curated
dataset containing a set of regular expressions generated from the
International Telecommunications Union (ITU) International Call Sign prefixes.
The registration codes in this dataset are separated by country post The Paris
Convention in 1929. The database also contains a description of each codeset
with 2 and 3 letter ISO country codes following the ISO-3166 standard.

## Installation

Flydenity is on PyPi, simply install it with PIP

  ```bash
  pip3 install flydenity
  ```

## Running the library

To run, you can simply include it in your python library using the following

  ```python
  from flydenity import parser
  identifer = parser.ARParser()
  nation_of_origin = ["AF1234"]
  ```

You can also run it from the command line

  ```bash
  $ flydenity AF1234
  {'AF1234': [{'nation': 'United States', 'description': 'general', 'iso codes': "['US', 'USA']"}]}
  ```

## Stats
In total, the dataset contains a total of 408 unique regular expressions to
describe aircraft tail numbers across 217 unique countries.

## Using the Data
Of course, everyone has a programming language of choice. Mine for this effort
was Python. I've including a wrapper class classed "ARP" which you can use to
parse through the expressions.

## Maritime
Since the ITU International Call Sign prefexies are universal across Aircraft
and Maritime Call Signs, we include functions within out API to parse Maritime
Call Signs as well.

## Testing
To evaluate how well the regular expressions work, we extracted unique tail
numbers from a years worth of air traffic from FlightRadar24.com In total,
we evaluated over 250k unique tail numbers against the regular expressions
to minimize duplicate tags. In total, the parser was around 98% accurate in
matching tail numbers to a specific country. Of course this could be
improved, but that's why this library is open-source :)

## Registration Numbers
All data was collected using open sources across the web, specifically using
the links below.
- https://en.wikipedia.org/wiki/Aircraft_registration
- https://en.wikipedia.org/wiki/Call_sign
- https://en.wikipedia.org/wiki/Airline_codes#ICAO_airline_designator
- https://en.wikipedia.org/wiki/List_of_aircraft_registration_prefixes
- https://www.cia.gov/library/publications/the-world-factbook/fields/2270.html
- https://en.wikipedia.org/wiki/ITU_prefix
- http://aircraft-registration-country-codes.blogspot.com/
- https://www.itu.int/en/ITU-R/terrestrial/fmd/Pages/call_sign_series.aspx

## Country Codes Extracted From
- https://countrycode.org/
- https://github.com/datasets/country-codes

## Datasets
I constructed two datasets (as of right now) for this effort.
1. processed_itu_countries_regex.csv
2. processed_itu_organizations_regex.csv


## Countries, Regions or Territories with No Standard
#### Compared to country list at https://countrycode.org/, there are a total of that are not included
Some of these countries  or regions could have a standard that is not within
this database. Please update the list if you make changes.
- Aland Islands (AX)
- American Samoa (AS)
- Antarctica(AQ)
- Bouvet Island	(BV)
- British Indian Ocean Territory (IO)
- Christmas Island (CX)
- Cocos (Keeling) Islands (CC)
- Curacao (CW)
- French Guiana	(GF)
- French Southern Territories (TF)
- Guadeloupe (GP)
- Guam (GU)
- Heard and Mcdonald Islands (HM)
- Jersey (JE)
- Martinique (MQ)
- Mayotte (YT)
- New Caledonia (NC)
- Niue (NU)
- Norfolk Island (NF)
- Northern Mariana Islands (MP)
- Pitcairn (PN)
- Puerto Rico (PR)
- Saint-Barthélemy (BL)
- Saint Martin (MF)
- Saint Pierre and Miquelon (PM)
- South Georgia and the South Sandwich Islands (GS)
- Svalbard and Jan Mayen Islands (SJ)
- Tokelau (TK)
- U.S. Outlying Islands (UM)
- U.S. Virgin Islands (VI)
- Wallis and Futuna (WF)
- Western Sahara (EH)


#### Contact

Collen Roller
collen.roller@gmail dot com
