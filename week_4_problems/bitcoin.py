import sys
import requests

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    api_key = "9b1785ba8b623d74c998a80c0bb913abd8c22567f91e3cae31aad321a66467c2" # Replace with your actual API key
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price_usd = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")
    except (KeyError, ValueError):
        sys.exit("Error parsing API response")

    total_cost = n * price_usd
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()