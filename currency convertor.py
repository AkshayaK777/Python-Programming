def convert_currency(usd_amount):
    rates = {
        "EUR": 0.92,
        "GBP": 0.79,
        "INR": 83.30,
        "JPY": 151.50
    }
    
    print(f"\n--- $ {usd_amount} USD is equal to: ---")
    for currency, rate in rates.items():
        print(f"{currency}: {usd_amount * rate:.2f}")

if __name__ == "__main__":
    try:
        amount = float(input("Enter amount in USD: $"))
        convert_currency(amount)
    except ValueError:
        print("Invalid input. Please enter a number.")