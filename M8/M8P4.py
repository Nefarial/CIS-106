filename = "orders.txt"

sum_ext = 0.0
count = 0

print(f"{'Item':<15}{'Qty':>6}{'Price':>12}{'Extended':>14}")

with open(filename, "r") as f:
    while True:
        item = f.readline()
        if not item:
            break
        item = item.strip()

        qty_line = f.readline()
        price_line = f.readline()
        if not qty_line or not price_line:
            break

        qty = int(qty_line.strip())
        price = float(price_line.strip())

        ext = qty * price
        sum_ext += ext
        count += 1

        print(f"{item:<15}{qty:>6}{price:>12.2f}{ext:>14.2f}")

avg_order = (sum_ext / count) if count > 0 else 0.0

print(f"\nSum of extended prices: ${sum_ext:,.2f}")
print(f"Number of orders: {count}")
print(f"Average order: ${avg_order:,.2f}")
