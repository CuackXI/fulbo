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

    Team.objects.create(api_id=data['Teams'][i]['team']['id'], Name=data['Teams'][i]['team']['name'],
                        Code=data['Teams'][i]['team']['code'], Country=data['Teams'][i]['team']['country'],
                        Image_URL=data['Teams'][i]['team']['logo'])