qty = int(input("Enter the number of books: "))
cost = float(input("Enter cost per book: "))

total = qty * cost
if total > 50:
    shipping = 0.00
else:
    shipping = 25.00

print(f"The total of your order is: ${total:.2f}")
print(f"The shipping cost is: ${shipping:.2f}")
