import re
txt = "abbslls abaabasabbbbab ab"
x = re.findall("ab{2,3}", txt)
print(x)