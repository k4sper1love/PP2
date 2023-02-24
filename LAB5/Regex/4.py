import re
txt = "Aeeeeses Aes Ae aEa aaa AAA A"
x = re.findall("[A-Z]{1}[a-z]+", txt)
print(x)