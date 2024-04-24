import json

file = open('ex5.json', 'r')
example = json.load(file)
file.close()  

for i in example:
    if i["name"] == "Old Fashioned" and i["type"] == "donut": 
        i["batter"].append({"id": "1005", "type": "Tea"})
        break

file = open('ex5.json', 'w')
json.dump(example, file, indent=2)
file.close()  