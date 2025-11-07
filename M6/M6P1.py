qty = int(input("Enter quantity of widgets: "))
if qty > 10000:
    price = 10.00
elif 5000 <= qty <= 10000:
    price = 20.00
else:
    price = 30.00

ext = qty * price
tax = ext * 0.07
total = ext + tax

print(f"Quantity: {qty}")
print(f"Unit price: ${price:.2f}")
print(f"Extended price: ${ext:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
