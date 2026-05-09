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

today = datetime.utcnow().date()

# PCS Giro results page
url = "https://www.procyclingstats.com/race/giro-d-italia/2025/results"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table")

stages = []

# Default empty winners
winner_map = {}

# Parse tables
for table in tables:

    rows = table.find_all("tr")

    for row in rows:

        cols = row.find_all("td")

        if len(cols) >= 4:

            stage_text = cols[1].get_text(strip=True)

            winner_text = cols[3].get_text(strip=True)

            # Detect "Stage X"
            if "Stage" in stage_text:

                try:
                    stage_number = stage_text.split("Stage")[1].strip()

                    winner_map[stage_number] = winner_text

                except:
                    pass

# Build stages
for i in range(1, 22):

    stage_date = datetime(2026, 5, i).date()

    if stage_date < today:
        status = "Finished"
    elif stage_date == today:
        status = "Live"
    else:
        status = "Upcoming"

    winner = winner_map.get(str(i), "")

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

# Final JSON structure
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

print(response.status_code)
print(response.text)
