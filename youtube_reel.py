import requests
import random

YOUTUBE_API_KEY = "AIzaSyAgBJCBNICS_qYCGTWcuH3ldCRUO4xw5bY"

search_terms = [
    "comida española",
    "frases en español",
    "cultura hispana",
    "aprender español",
    "español para principiantes",
    "jerga española",
    "viajar en España",
    "música en español"
]

def get_spanish_reel():
    query = random.choice(search_terms)
    search_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "videoDuration": "short",
        "videoEmbeddable": "true",
        "maxResults": 10,
        "key": YOUTUBE_API_KEY
    }

    try:
        response = requests.get(search_url, params=params)
        results = response.json().get("items", [])

        if not results:
            return "⚠️ No reels found. Try again soon."

        video = random.choice(results)
        video_id = video["id"]["videoId"]
        return f"https://youtube.com/shorts/{video_id}"

    except Exception as e:
        return f"🔥 YouTube Error: {str(e)}"

