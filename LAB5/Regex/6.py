import re
txt = "hello, qwerty."
x = re.sub("[., ]", ":", txt)
print(x)