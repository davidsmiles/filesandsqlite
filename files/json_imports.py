import json

with open('friends_json.txt', 'r') as file:
    contents = json.load(file)

print(contents)

cars = {
    "cars": [
        {"make": "Ford", "model": "Fiesta"},
        {"make": "Ford", "model": "Fiesta"}
    ]
}

with open('cars_json.txt', 'r') as cars_file:
    print(json.load(cars_file))