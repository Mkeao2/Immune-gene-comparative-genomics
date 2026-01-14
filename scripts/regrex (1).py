#!/usr/bin/env python3 

import re

f = open('FlyImmuneGenes.txt', encoding='utf-8')
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall("parent=(.*),FBtr", f.read())
#write to file
with open("bonelees_output.txt", "w", encoding="utf-8") as outfile:
         for string in strings:
                       outfile.write(f"{string}\n")
