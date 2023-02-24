import re
def snakeToCamel(str):
    if str[0] == "_" or str[len(str)-1] == "_":
        return None
    x = re.split("_", str)
    for i in range(1, len(x)):
        x[i] = x[i].capitalize()
    return "".join(x)

print(snakeToCamel("_check_snake"))
print(snakeToCamel("check_snake_"))
print(snakeToCamel("check_snake"))
print(snakeToCamel("check_snake_to_camel"))
