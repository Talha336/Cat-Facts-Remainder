import requests
import time
from pushbullet import Pushbullet

# Initialize Pushbullet with your API key
api_key = "o.8XK5Zssn78Z0gUho7oPxjeoquuTNoUvt"
pb = Pushbullet(api_key)

# Function to fetch a random cat fact
def fetch_cat_fact():
    cat_facts = requests.get("https://catfact.ninja/fact")
    if cat_facts.status_code == 200:
        return cat_facts.json()["fact"]
    else:
        return "Failed to fetch cat fact"

# Main loop to display cat facts and send notifications every 5 seconds
while True:
    # Fetch a random cat fact
    fact = fetch_cat_fact()
    
    # Send notification with the cat fact
    pb.push_note("Cat Fact", fact)
    
    # Wait for 5 seconds before fetching the next fact
    time.sleep(5)
