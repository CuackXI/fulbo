import json
from models import Team

# Open the JSON file
with open('TeamsNStadiums.json', 'r') as file:
    # Load JSON data from file
    data = json.load(file)

for i in range(len(data['Teams'])):
    print(data['Teams'][i]['team']['id'])
    print(data['Teams'][i]['team']['name'])
    print(data['Teams'][i]['team']['code'])
    print(data['Teams'][i]['team']['country'])
    print(data['Teams'][i]['team']['logo'])

