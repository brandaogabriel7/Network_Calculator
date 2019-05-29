import json

def read_json(filename):
    with open(filename + '.json', 'r') as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename + '.json', 'w') as f:
        json.dump(data, f)