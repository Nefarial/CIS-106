item = input("Enter item (A or B): ")
qty = int(input("Enter the quantity: "))
if item == "A":
    uprice = 10.00
else:
    uprice = 20.00

extprice = qty * uprice

print(f"Item: {item}")
print(f"Unit price: ${uprice:.2f}")
print(f"Extended price: ${extprice:.2f}")
