
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve YouTube API key
api_key = os.getenv("YOUTUBE_API_KEY")

if not api_key:
    raise ValueError("YOUTUBE_API_KEY is missing from .env")

# YouTube API endpoint
url = "https://www.googleapis.com/youtube/v3/channels"

# URL query parameters
params = {
    "part": "contentDetails",
    "forHandle": "MrBeast",
    "key": api_key
}

# Send GET request
response = requests.get(url, params=params, timeout=30)

# Raise error if request fails
response.raise_for_status()

# Convert JSON response to Python dictionary
data = response.json()

print(data)
