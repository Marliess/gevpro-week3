#!/usr/bin/env python

import sys
from xml.dom import minidom

def main():
    doc = minidom.parse("spontal.xml")
    name = doc.getElementsByTagName("FO_START")[0]
    print(name.firstChild.data)


main()

