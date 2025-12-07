def compute_discount(qty, price, disc_rate):
    ext_price = qty * price
    disc_amt = ext_price * disc_rate
    disc_price = ext_price - disc_amt
    return disc_amt, disc_price

qty = int(input("Enter quantity: "))
price = float(input("Enter unit price: "))
disc_rate = float(input("Enter discount rate (as decimal, e.g. 0.10): "))

disc_amt, disc_price = compute_discount(qty, price, disc_rate)

print("\nQuantity  Price      Discount   Discounted Total")
print("-" * 50)
print(f"{qty:8d}  ${price:8.2f}  ${disc_amt:8.2f}  ${disc_price:14.2f}")
