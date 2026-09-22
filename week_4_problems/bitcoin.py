import requests
import json
import sys

if len(sys.argv) >= 2:
    n = float(sys.argv[1])
    API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    try:
        price = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}")
    except requests.RequestException:
        ...
    usd = float(price.json()["data"]["priceUsd"])
    print(f"${n * usd:,.4f}")