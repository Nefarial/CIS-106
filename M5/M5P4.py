appliance = input("Enter appliance name: ")
price = float(input("Enter appliance cost: "))

if price > 1000:
    warranty = price * .10
else:
    warranty = price * .05

total = price + warranty

print(f"Appliance: {appliance}")
print(f"{appliance} price: ${price:.2f}")
print(f"Warranty cost: ${warranty:.2f}")
print(f"Total cost: ${total:.2f}")
