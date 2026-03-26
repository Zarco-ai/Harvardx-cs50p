#my original code for bitcoin
import sys
import requests
import json

def main():
    try:
        x = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(0)
    except IndexError:
        print("Missing command-line argument")
        sys.exit(0)
    print(x)
###Updated Code

    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=90faae277719844b030b539c0871526f378e2467efbb24b891e88723068a2fee"

    # The exception block must wrap the network request, not the variable assignment
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

    except requests.exceptions.RequestException as e:
        # This catches all network errors (e.g., connection, timeout, DNS)
        sys.exit(f"API Request Failed: {e}")

    # --- 3. Process the Data ---
    try:
        data = response.json()

        # CoinCap returns the price as a string in the nested 'priceUsd' key
        price_usd_str = data['data'][0]['priceUsd']
        current_price = float(price_usd_str)

    except (json.JSONDecodeError, KeyError, IndexError, ValueError):
        # This catches errors if the API returns malformed JSON or unexpected data structure
        sys.exit("Error: Could not parse price data from API response.")

    # --- 4. Calculate and Print Result ---
    total_value = x * current_price

    # Example Output: 0.5 BTC is worth $15,000.00 (assuming price of $30,000)
    print(f"{2:.2f} BTC is worth ${total_value:,.2f} USD.")




main()
