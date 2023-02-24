import re
def camelToSnake(str):
    x = re.sub(r"([a-z])([A-Z])", r"\1_\2", str).lower()
    return x

print(camelToSnake("CamelToSnake"))
print(camelToSnake("camelToSnake"))