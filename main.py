import requests
import os

hub_text = requests.get("https://api.github.com/zen").text

print("hello")
gh_code = os.environ["GH_TOKEN"]
yt_code = os.environ["YT_API_KEY"]

print(f"{gh_code} and {yt_code}")
