import re
txt = "hello abba_baba ab_baaa b_baa _bab"
x = re.findall("[a-z]+_[a-z]+", txt)
print(x)