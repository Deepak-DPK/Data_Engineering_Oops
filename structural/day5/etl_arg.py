#currency has default value of "USD"

def format_price(amount, currency="USD"):
    return f"{amount} {currency}"

print(format_price(100,"EUR"))  # Output: EUR 100
print(format_price(50))         # Output: USD 50 (Used the default!
