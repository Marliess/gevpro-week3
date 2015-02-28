#!/usr/bin/env python

import sys
import urllib
import json


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
    data = [] 
    #data = [(for line in j
    for line in j:
        blood = ((line)[2])
        die = ((line)[3])
        if blood == die:
            print(blood,"______",die)
            #data.append(line)
    #print(data)

if __name__ == "__main__":
    main()
