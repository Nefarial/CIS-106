part = input("Enter part number : ").strip()
qty  = int(input("Enter quantity: "))

if part in ("10", "55"):
    unit_cost = 1.00
elif part == "99":
    unit_cost = 2.00
elif part in ("80", "70", "40"):
    unit_cost = 3.00
else:
    unit_cost = 5.00

total = qty * unit_cost

print(f"Part: {part}")
print(f"Unit cost: ${unit_cost:.2f}")
print(f"Total cost: ${total:.2f}")
