import re
txt = "a5512o512oSAdaslzcmscaq ddfk bb"
x = re.search("^a.*b$", txt)
print(x)