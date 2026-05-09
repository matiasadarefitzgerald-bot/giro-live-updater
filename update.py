import requests
import os
 
JSONBIN_URL = "https://api.jsonbin.io/v3/b/69fe2434c0954111d8f6bd0b"

MASTER_KEY = os.environ["JSONBIN_KEY"]

headers = {
    "Content-Type": "application/json",
    "X-Master-Key": MASTER_KEY
}

# Example automatic data
# Later this becomes real API data

data = {
    "race": "Giro d'Italia",
    "last_updated": "AUTO",
    "stages": [
        {
            "stage": "1",
            "status": "Finished",
            "utah_start": "5:30 AM",
            "utah_finish": "10:45 AM",
            "winner": "Actual Winner",
            "gc": "Actual GC",
            "kom": "Actual KOM",
            "points": "Actual Points",
            "youth": "Actual Youth",
            "avg_speed": "44.1 km/h"
        }
    ]
}

response = requests.put(
    JSONBIN_URL,
    headers=headers,
    json=data
)

print(response.text)
