import json

# Python dictionary
student = {
    "name": "Nissy",
    "age": 18,
    "course": "CSE"
}

# Convert Python dict to JSON string
json_data = json.dumps(student)

print("JSON format:")
print(json_data)

# Convert JSON back to Python dictionary
python_data = json.loads(json_data)

print("Back to Python dictionary:")
print(python_data)
