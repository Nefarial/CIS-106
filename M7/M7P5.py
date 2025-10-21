answer = input("Do you want to enter an order? Yes/No: ")

sum_discounts = 0.0

while answer == "Yes":
    qty = int(input("Enter quantity: "))
    price = float(input("Enter unit price: "))

    extended = qty * price

    if extended > 10000:
        disc_price = 0.25
    else:
        disc_price = 0.10

    discount = extended * disc_price
    total = extended - discount

    print(f"Extended price: ${extended:.2f}")
    print(f"Discount amount: ${discount:.2f}")
    print(f"Total: ${total:.2f}")
    print()

    sum_discounts += discount
    answer = input("Enter another order? Yes/No: ")

print(f"Sum of all discounts: ${sum_discounts:.2f}")
