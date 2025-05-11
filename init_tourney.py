import requests
import config
from datetime import datetime, timedelta


url = f"https://lichess.org/api/swiss/new/{config.TEAM_ID}"
headers = {
    "Authorization": f"Bearer {config.API_TOKEN}",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "name": "Friendly Blitz Showdown",
    "clock.limit": 15,
    "clock.increment": 3,
    "nbRounds": 3,
    "roundInterval": 45,
    "variant": "standard",
    "description": "A fun blitz event for team members!",
    "rated": "true"
}

# Send the request
response = requests.post(url, headers=headers, data=data)

# Handle response
if response.status_code == 200:
    print("Tournament created successfully!")
    print(response.json())
else:
    print("Failed to create tournament")
    print("Status code:", response.status_code)
    print("Response:", response.text)
