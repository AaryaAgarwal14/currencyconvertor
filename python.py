import requests

def currency_converter():
    print("===== GLOBAL CURRENCY CONVERTER =====")

    try:
        # Fetch available currencies and rates
        response = requests.get(
            "https://open.er-api.com/v6/latest/USD",
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        if data.get("result") != "success":
            print("Unable to fetch exchange rates.")
            return

        rates = data["rates"]

        print("Available currency codes:")
        print(", ".join(sorted(rates.keys())))

        amount = float(input("\nEnter amount: "))
        from_currency = input("Convert from (e.g. INR): ").upper()
        to_currency = input("Convert to (e.g. KRW): ").upper()

        if amount < 0:
            print("Amount cannot be negative.")
        elif from_currency not in rates or to_currency not in rates:
            print("Invalid currency code.")
        else:
            # Rates are based on USD
            amount_in_usd = amount / rates[from_currency]
            converted_amount = amount_in_usd * rates[to_currency]

            print(f"\n{amount:.2f} {from_currency} = "
                  f"{converted_amount:.2f} {to_currency}")

    except ValueError:
        print("Please enter a valid numeric amount.")
    except requests.RequestException as error:
        print("Network or API error:", error)

currency_converter()