#!/usr/bin/env python

import sys
import urllib
import json
from collections import namedtuple


"""
1. .json inlezen
2. lijst maken van alle talen en hun classificaties waar tenminste
    een van de woorden voor "bloed" identiek is aan een van de
    woorden voor "sterven"
3. List comprehension gebruiken voor lijst van resultaten
4. elk element in de lijst moet een named tuple zijn

Bestand openen: json.load()
Bestand opslaan: json.dump()

"""

def main():
    url = open("blood-die.json")
    j = json.load(url) 
    data = [print(line) for line in j if ((line)[2]) == ((line)[3])]
    """
    for line in j:
        #print(((line)[2]))              # blood = ((line)[2])
        #print(((line)[3]))              # die = ((line)[3])
        if ((line)[2]) == ((line)[3]):
            print(blood,"______",die)
            data.append(line)"""
    print(data)

if __name__ == "__main__":
    main()
