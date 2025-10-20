# name = "田中太郎"

# print(len(name))
# print(name[0])
# print(name[1:3])
# print(name + "さん")

import json

person = {
    "name": "田中太郎",
    "age": 30,
    "city": "東京"
}

# json_text = json.dumps(person)
# print(json_text)

# person = json.loads(json_text)
# print(person)

print(person[1])