import json as js

x = {
    "name": "Dhana Chowdary",
    "age": 22,
    "City": "Mandadhi",
    "Pets": None,
    "Cars": ["BMW", "Audi", "Mercedes"],
    "isEmployed": True
}

y = js.dumps(x, indent=2)
print(y)
