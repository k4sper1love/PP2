import re
txt = "abbslls abaaasabbbb ab"
x = re.findall("ab*", txt)
print(x)