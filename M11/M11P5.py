total = 0.0
tax = 0.0

def compute_total_and_tax(qty, price):
    global total, tax
    total = qty * price
    tax = total * 0.07

again = input("Do you want to enter an order (Yes or No)? ")

print(f"\n{'Qty':>5}{'Price':>10}{'Total':>12}{'Tax':>10}")
print("-" * 37)

sum_total = 0.0
sum_tax = 0.0

while again.strip().lower() == "yes":
    qty = int(input("Enter quantity: "))
    price = float(input("Enter unit price: "))

    compute_total_and_tax(qty, price)

    print(f"{qty:5d}${price:9.2f}${total:11.2f}${tax:9.2f}")

    sum_total += total
    sum_tax += tax

    again = input("Do you want to enter another order (Yes or No)? ")

print("-" * 37)
print(f"{'SUMS':>5}{'':>10}${sum_total:11.2f}${sum_tax:9.2f}")
