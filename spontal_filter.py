#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

"""
1. corpus inlezen
2. datapoints controleren
3. foutieve datapoints verwijderen
4. corpus naar bestand schrijven
"""

def main():
    tree = ET.parse("spontal.xml")
    root = tree.getroot()
    for point in root.findall("point"):
        FO_END = float(point.find("FO_END").text)                       #child[12].text
        FO_START = float(point.find("FO_START").text)                   #child[13].text
        TOP_HZ = float(point.find("TOP_HZ").text)                       #child[7].text
        BOTTOM_HZ = float(point.find("BOTTOM_HZ").text)                 #child[5].text
        if FO_END > BOTTOM_HZ and FO_START < TOP_HZ:
            tree.write("spontal_filtered.xml")

        if FO_END < BOTTOM_HZ or FO_START > TOP_HZ:
            root.remove(point)
        if FO_START > TOP_HZ or FO_START < BOTTOM_HZ:
            root.remove(point)


            
if __name__ == "__main__":
    main()

