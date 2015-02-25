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
    for child in root:
        FO_END = child[12].text
        FO_START = child[13].text
        TOP_HZ = child[7].text
        BOTTOM_HZ = child[5].text
        if FO_END > TOP_HZ and FO_END < BOTTOM_HZ:
            root.remove("FO_END")
        else:
            tree.write("spontal_filtered.xml")
        if FO_START < BOTTOM_HZ and FO_START > TOP_HZ:
            root.remove("FO_START")
        else:
            tree.write("spontal_filtered.xml")


if __name__ == "__main__":
    main()

