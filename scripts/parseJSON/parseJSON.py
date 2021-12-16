import json
data = '''{
    "name": "Jason",
    "email": {
        "hide": "yes"
    }
}'''

info = json.loads(data)
#info is a dictionary
print(info["name"])
print(info["email"]["hide"])
