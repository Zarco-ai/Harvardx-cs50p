import sys
import requests
import json

def main():
    # --- 1. Validate Command-Line Argument ---
    # Must have exactly one argument after the script name (sys.argv[0])
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        # Get the number of bitcoin from the command line and convert it to a float
        btc_amount = float(sys.argv[1])

        # Ensure the amount is non-negative
        if btc_amount < 0:
            sys.exit("Bitcoin amount must be a non-negative number.")

    except ValueError:
        # Exit if the argument cannot be converted to a float
        sys.exit("Command-line argument is not a valid number.")

    # --- 2. Query the API ---
    # NOTE: Replace "YourApiKey" with your actual CoinCap API key.
    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=90faae277719844b030b539c0871526f378e2467efbb24b891e88723068a2fee"

    try:
        response = requests.get(url)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        # Catch all network/request errors
        sys.exit(f"API Request Failed: {e}")

    # --- 3. Process the Data ---
    try:
        data = response.json()

        # Access the price string via the nested keys
        price_usd_str = data['data']['priceUsd']
        current_price = float(price_usd_str)

    except (json.JSONDecodeError, KeyError, IndexError, ValueError):
        # Catch errors if the JSON is bad or the structure is wrong
        sys.exit("Error: Could not parse price data from API response.")

    # --- 4. Calculate and Print Result ---
    total_value = btc_amount * current_price

    # Use a standard f-string for output formatting:
    # $ : Prefix with a dollar sign
    # , : Use a comma as the thousands separator
    # .4f : Format as a float with exactly four decimal places
    print(f"${total_value:,.4f}")

if __name__ == "__main__":
    main()
