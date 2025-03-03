file_path = "currency.csv"  

currency_dict = {}

with open(file_path, "r", encoding="ISO-8859-1") as file:
    next(file)  
    for line in file:
        parts = line.strip().split(",")  
        if len(parts) == 3:  
            code, name, rate = parts
            currency_dict[code.upper()] = {"name": name, "rate": float(rate)}


usd_amount = float(input("How much dollar do you have?: "))
currency_code = input("What currency you want to have?: ").strip().upper()


if currency_code in currency_dict:
    exchange_rate = currency_dict[currency_code]["rate"]
    converted_amount = usd_amount * exchange_rate
    currency_name = currency_dict[currency_code]["name"]

    print(f"\nDollar: {usd_amount} USD")
    print(f"{currency_name}: {converted_amount:.6f} {currency_code}")
else:
    print("Currency not found. Please enter a valid currency code.")
