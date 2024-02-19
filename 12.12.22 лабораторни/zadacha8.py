import json
dictionary = {
    "name": "kristian",
    "rollno": 56,
    "phonenumber": "0883677050"
}

with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)