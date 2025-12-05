def calc_ext_price(qty, unit_price):
    """Return extended price, with 10% discount if > 10,000."""
    ext_price = qty * unit_price
    if ext_price > 10000.00:
        ext_price = ext_price * 0.90
    return ext_price

print("Qty   Unit Price   Ext Price")
print("-" * 30)
total_ext = 0.0
again = "Y"

while again.upper() == "Y":
    qty = int(input("Enter quantity (0 to stop): "))
    unit_price = float(input("Enter unit price: "))
    ext_price = calc_ext_price(qty, unit_price)
    total_ext += ext_price
    print(f"{qty:>3d}   ${unit_price:>9.2f}   ${ext_price:>9.2f}")
    again = input("Do you want to enter another item? (Y/N): ")
    
print("-" * 30)
print(f"Total extended price for all items: ${total_ext:,.2f}")
