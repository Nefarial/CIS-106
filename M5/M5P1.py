qty = int(input("Enter quantity: "))

if qty >= 1000:
    uprice = 3.00
else:
    uprice = 5.00

extprice = qty * uprice

tax = extprice *.07

total = extprice + tax

print(f"Quantity: {qty}")
print(f"Unit price: ${uprice:.2f}")
print(f"Extended price: ${extprice:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total price: ${total:.2f}")
