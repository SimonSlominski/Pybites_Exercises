"""
Bite 180. Group names by country

In this Bite you are presented with a list of surnames, names, and countries.
These 3 fields are in a multiline string, separated by a comma.

Code group_names_by_country, looping through the list, returning a collections.defaultdict
where the keys are countries and the values are lists of concatenated names and surnames.
The order of the keys (countries) and the value lists (names) does not matter.
"""

from collections import defaultdict


data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)

    for line in data.splitlines()[1:]:
        last_name, first_name, country_code = line.split(',')
        name = f'{first_name} {last_name}'
        countries[country_code].append(name)

    return countries
