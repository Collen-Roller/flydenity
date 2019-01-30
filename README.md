# Aircraft Registration Prefix (ARP) Dataset

This dataset contains country specific aircraft registration code expressions separated by country. The database also contains a description of each codeset with both 2 and 3 letter ISO country codes following the ISO-3166 standard.

## Stats
In total, the dataset contains a total of 408 unique regular expressions to describe aircraft tail numbers across 217 unique countries. 

## Using the Data
Of course, everyone has a programming language of choice. Mine for this effort was Python. I've including a wrapper class classed "ARP" which you can use to parse through the expressions.

## Testing
To evaluate how well the regular expressions work, we extracted unique tail numbers from a years worth of air traffic from FlightRadar24.com In total, we evaluated over 250k unique tail numbers against the regular expressions to minimize duplicate tags. In total, the parser was around 98% accurate in matching tail numbers to a specific country. Of course this could be improved, but that's why this library is open-source :)

## Registration Numbers
All data was collected using open sources across the web, specifically using the links below.
- https://en.wikipedia.org/wiki/Aircraft_registration
- https://en.wikipedia.org/wiki/Call_sign
- https://en.wikipedia.org/wiki/Airline_codes#ICAO_airline_designator
- https://en.wikipedia.org/wiki/List_of_aircraft_registration_prefixes
- https://www.cia.gov/library/publications/the-world-factbook/fields/2270.html
- https://en.wikipedia.org/wiki/ITU_prefix
- http://aircraft-registration-country-codes.blogspot.com/

## Country Codes Extracted From
- https://countrycode.org/
- https://github.com/datasets/country-codes

## Datasets
I constructed two datasets (as of right now) for this effort. 
1. processed_itu_countries_regex.csv
2. processed_itu_organizations_regex.csv


## Countries, Regions or Territories with No Standard
#### Compared to country list at https://countrycode.org/, there are a total of that are not included
Some of these countries  or regions could have a standard that is not within this database. Please update the list if you make changes. 
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

## Dashes
#### Countries that do not use dashes (with dashes in the id)
- Anguilla (VP-A)
- Bermuda (VP-B, VQ-B, VR-B)
- British Virgin Islands (VP-L)
- Cayman Islands (VP-C)
- Falk Islands (VP-F)
- Faroe Islands (OY-H)
- French Poly (F-OH)
- Gibraltar (VP-G)
- Greenland (OY-H)
- Hong Kong (B-H, B-K, B-L)
- Macau (B-M)
- Montserrat (VP-M)
- Palestinian Authority (SU-Y)
- Reunion Island (F-OD)
- Saint Helena (VQ-H)
- Turks and Caicos (VQ-T)

#### Countries that do not use dashes (without dashes in the id)
- Japan (JA)
- South Korea (HL)
- United States 
- Ukraine for numbers between 10K and 99K
- Uzbekistan
- Venezuela

#### Countries with dash in suffix
- Macedonia (Z3)



#### Contact

Collen Roller 
collen.roller@gmail.com
