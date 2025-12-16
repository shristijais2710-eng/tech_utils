import requests
import json
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def get_exchange_rate():
    """Fetch USD to INR exchange rate"""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "rates" not in data or "INR" not in data["rates"]:
            raise KeyError("INR rate not found")

        usd_to_inr = data["rates"]["INR"]
        return usd_to_inr

    except Exception as e:
        print("❌ Error fetching exchange rate:", e)
        return None


def convert_inr_to_usd(amount_inr, usd_to_inr):
    """Convert INR to USD"""
    return amount_inr / usd_to_inr


def convert_usd_to_inr(amount_usd, usd_to_inr):
    """Convert USD to INR"""
    return amount_usd * usd_to_inr


# -------------------------
# MAIN PROGRAM
# -------------------------
if __name__ == "__main__":
    print("=== Currency Converter ===")
    print("1. INR ➝ USD")
    print("2. USD ➝ INR")

    choice = input("Choose option (1/2): ")

    rate = get_exchange_rate()

    if rate is None:
        print("❌ Conversion failed. Try again later.")
        exit()

    try:
        if choice == "1":
            amount = float(input("Enter amount in INR (₹): "))
            usd = convert_inr_to_usd(amount, rate)
            print(f"\n₹{amount:,.2f} = ${usd:,.2f}")
            print(f"Rate: 1 USD = ₹{rate:.2f}")

        elif choice == "2":
            amount = float(input("Enter amount in USD ($): "))
            inr = convert_usd_to_inr(amount, rate)
            print(f"\n${amount:,.2f} = ₹{inr:,.2f}")
            print(f"Rate: 1 USD = ₹{rate:.2f}")

        else:
            print("❌ Invalid choice. Please select 1 or 2.")

    except ValueError:
        print("❌ Please enter a valid number.")
