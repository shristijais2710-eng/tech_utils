import requests
import json

def convert_inr_to_usd_api(amount_inr):
    """Convert INR to USD using real-time exchange rates"""
    try:
        # Using ExchangeRate-API (free tier available)
        API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
        
        # Make API request
        response = requests.get(API_URL)
        data = response.json()
        
        # Get exchange rates
        usd_to_inr = data['rates']['INR']  # 1 USD = X INR
        inr_to_usd = 1 / usd_to_inr  # 1 INR = X USD
        
        # Convert the amount
        amount_usd = amount_inr * inr_to_usd
        
        return amount_usd, inr_to_usd
    
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
        return None, None

# Usage
if __name__ == "__main__":
    try:
        amount = float(input("Enter amount in INR: ₹"))
        usd_amount, rate = convert_inr_to_usd_api(amount)
        
        if usd_amount:
            print(f"\n₹{amount:,.2f} = ${usd_amount:,.2f}")
            print(f"Exchange rate: 1 INR = ${rate:.6f}")
            print(f"Exchange rate: 1 USD = ₹{1/rate:.2f}")
    
    except ValueError:
        print("Please enter a valid number")