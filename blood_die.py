#!/usr/bin/env python

import sys
import json
from collections import namedtuple


def main():
    """Json inlezen"""
    data = open("blood-die.json")
    j = json.load(data)
    dataList = []
    """Namedtuple gemaakt met de elementen in het json bestand"""
    landenlijst = namedtuple("Land","taal,classificatie,bloed,sterf")
    for lijst in j:
        land = lijst[0]
        classificatie = lijst[1]
        bloeden = lijst[2].split(",")
        sterven = lijst[3].split(",")
        """List comprehension van alle talen en hun classificaties waar tenminste
    1 woord voor "bloed" gelijk is aan tenminste 1 woord voor "sterven" """
        [dataList.append(landenlijst(land,classificatie,bloeden,sterven)) for bloed in bloeden if bloed in sterven]
    print(dataList)
    
if __name__ == "__main__":
    main()
