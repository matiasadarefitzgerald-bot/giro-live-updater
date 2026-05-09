import requests
import os
from datetime import datetime
from bs4 import BeautifulSoup

# JSONBin settings
JSONBIN_URL = "https://api.jsonbin.io/v3/b/69fe2434c0954111d8f6bd0b"

MASTER_KEY = os.environ["JSONBIN_KEY"]

headers = {
    "Content-Type": "application/json",
    "X-Master-Key": MASTER_KEY
}

# Today's date
today = datetime.utcnow().date()

# Example race source
url = "https://en.wikipedia.org/wiki/2025_Giro_d%27Italia"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Placeholder parsing
# We improve this later

stages = []

for i in range(1, 22):

    stage_date = datetime(2026, 5, i).date()

    if stage_date < today:
        status = "Finished"
    elif stage_date == today:
        status = "Live"
    else:
        status = "Upcoming"

    winner = ""

    # Example automatic winner logic
    if status == "Finished":
        winner = "Stage Completed"

    stages.append({
        "stage": str(i),
        "status": status,
        "utah_start": "5:30 AM",
        "utah_finish": "10:45 AM",
        "winner": winner,
        "gc": "",
        "kom": "",
        "points": "",
        "youth": "",
        "avg_speed": ""
    })

data = {
    "race": "Giro d'Italia",
    "last_updated": str(datetime.utcnow()),
    "stages": stages
}

# Push update to JSONBin
response = requests.put(
    JSONBIN_URL,
    headers=headers,
    json=data
)

print(response.status_code)
print(response.text)
