import re
txt = "LoremIpsumDolorSitAmet"
# x = re.sub(r"([A-Z])([a-z]*)", r"\1\2 ", txt)
x = re.sub(r"([a-z])([A-Z])", r"\1 \2", txt)
print(x)