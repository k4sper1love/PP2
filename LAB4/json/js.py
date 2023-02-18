import json
f = open('LAB4/json/sample_data.json')
data = json.load(f)
json_print = []
for x in data['imdata']:
    for y in x:
        json_print.append([x[y]["attributes"]['dn'], x[y]["attributes"]['speed'], x[y]["attributes"]['mtu']])

print("""Interface Status
================================================================================
DN                                                 Description            Speed   MTU  
-------------------------------------------------- --------------------  -------  ----""")
for x in json_print:
    print(f"{x[0] : <43}", " " * 26, f"{x[1] : ^11}{x[2] : <0}")