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
    for POINT in root.findall("POINT"):
        FO_END = float(POINT.find("F0_END").text)   
        FO_START = float(POINT.find("F0_START").text)
        TOP_HZ = float(POINT.find("TOP_HZ").text)       
        BOTTOM_HZ = float(POINT.find("BOTTOM_HZ").text)
        if FO_END < BOTTOM_HZ:
            root.remove(POINT)
        if FO_START > TOP_HZ:
            root.remove(POINT)
    tree.write("spontal_filtered.xml")




            
if __name__ == "__main__":
    main()

