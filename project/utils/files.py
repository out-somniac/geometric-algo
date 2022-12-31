import json

def save_points_to_file(points, name):
    jsonString = json.dumps(points)
    with open(name, 'w') as f:
        f.write(jsonString)

def get_saved_points(name):
    with open(name, 'r') as f:
        jsonContent = f.read()
    points = json.loads(jsonContent)
    return points