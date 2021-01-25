import json
import requests

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)


json_string = json.dumps(data)
print(json_string)

dump = json.dumps(data, indent=4)
print(dump)

blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
print(encoded_hand)

decoded_hand = json.loads(encoded_hand)
print(decoded_hand)


with open("data_file.json", "r") as read_file:
    data1 = json.loads(read_file.read())

print(data1)
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data1 = json.loads(json_string)
print(data1)

response1 = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response1.text)
