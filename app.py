import requests
import streamlit as st
import json

# Function to fetch data from CoinMarketCap API
def fetch_coin_data(symbol):
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbol}&convert=USD&CMC_PRO_API_KEY=839f226f-7a3d-49e4-8c10-56a444bd2c60"
    response = requests.get(url)
    data = response.json()
    return data

# Main function to run the Streamlit web app
def main():
    st.title("Cryptocurrency Price Checker")

    # User input for cryptocurrency symbol
    symbol = st.text_input("Enter a cryptocurrency symbol (e.g., BTC, ETH, ADA):")

    if st.button("Get Price"):
        if symbol:
            coin_data = fetch_coin_data(symbol.upper())  # Convert symbol to uppercase
            if "data" in coin_data:
                coin_info = coin_data["data"][symbol.upper()]
                price = coin_info["quote"]["USD"]["price"]
                st.success(f"The current price of {symbol.upper()} is ${round(price, 2)} USD")
            else:
                st.error("Invalid cryptocurrency symbol. Please enter a valid symbol.")
        else:
            st.warning("Please enter a cryptocurrency symbol.")

if __name__ == "__main__":
    main()


