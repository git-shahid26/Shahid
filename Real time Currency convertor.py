from forex_python.converter import CurrencyRates
import time

def get_exchange_rates():
    """
    Fetches and returns the latest exchange rates.
    """
    currency_rates = CurrencyRates()
    rates = currency_rates.get_rates('USD')  # Base currency is USD in this example
    return rates

def convert_currency(amount, from_currency, to_currency, exchange_rates):
    """
    Converts the given amount from one currency to another using the provided exchange rates.
    """
    if from_currency == to_currency:
        return amount

    try:
        rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * rate
        return converted_amount
    except KeyError:
        print("Invalid currency code. Please check your inputs.")
        return None

def main():
    while True:
        try:
            exchange_rates = get_exchange_rates()

            # Display available currencies
            print("Available currencies:")
            for currency, rate in exchange_rates.items():
                print(f"{currency}: {rate}")

            # Input conversion details
            amount = float(input("Enter the amount to convert: "))
            from_currency = input("Enter the source currency code: ").upper()
            to_currency = input("Enter the target currency code: ").upper()

            # Perform the conversion
            converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)

            if converted_amount is not None:
                print(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait for some time before fetching the latest rates again
        time.sleep(5)

if __name__ == "__main__":
    main()
