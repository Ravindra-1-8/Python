#Problem 5: Basic Currency Converter
#input: amount_in_usd = 100m exchange_rate_usd_to_eur = 0.85.   outputf: Equivalent amount in EUR: 85.0

a = int(input("amount_in_usd: "))
b = float(input("exchange_rate_usd_to_eur: "))

c =b * a
print(f"Equivalent amount in EUR: ",c)