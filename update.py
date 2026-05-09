import requests
import os
from datetime import datetime

# JSONBin settings
JSONBIN_URL = "https://api.jsonbin.io/v3/b/69fe2434c0954111d8f6bd0b"

MASTER_KEY = os.environ["JSONBIN_KEY"]

headers = {
    "Content-Type": "application/json",
    "X-Master-Key": MASTER_KEY
}

# Current UTC date
today = datetime.utcnow().date()

# Build stage data automatically
stages = []

for i in range(1, 22):

    # Example Giro stage dates
    # Adjust later for exact race calendar
    stage_date = datetime(2026, 5, i).date()

    # Automatic stage status
    if stage_date < today:
        status = "Finished"
    elif stage_date == today:
        status = "Live"
    else:
        status = "Upcoming"

    # Example automatic data structure
    stages.append({
        "stage": str(i),
        "status": status,
        "utah_start": "5:30 AM",
        "utah_finish": "10:45 AM",
        "winner": "",
        "gc": "",
        "kom": "",
        "points": "",
        "youth": "",
        "avg_speed": ""
    })

# Full race data
data = {
    "race": "Giro d'Italia",
    "last_updated": str(datetime.utcnow()),
    "stages": stages
}

# Update JSONBin
response = requests.put(
    JSONBIN_URL,
    headers=headers,
    json=data
)

# Output response
print(response.status_code)
print(response.text)
