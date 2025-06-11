from pprint import pprint

inf = [
    {"from": "B", "to": "E"},
    {"from": "A", "to": "C"},
    {"from": "F", "to": "B"},
    {"from": "D", "to": "A"},
    {"from": "C", "to": "F"},
]

names, values = [], []
for i in inf:
    names.append(i["from"])
    values.append(i["to"])

# new_inf = sorted(inf, key=lambda x: x["to"])[0]
#
# print(new_inf["from"])

[start] = [i for i in names if i not in values]

newData = []
cur = ""

while len(newData) != len(inf):
    for el in inf:
        if newData == [] and el.get("from") == start:
            newData.append(el)
            cur = el["to"]
        else:
            if el.get("from") == cur:
                newData.append(el)
                cur = el["to"]

pprint(newData)