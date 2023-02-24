import re
txt = "AsdasdNenenenLllBASksksk"
# x = re.split("[A-Z]", txt)
# print(x)
x = re.findall("[A-Z][^A-Z]*", txt)
print(x)