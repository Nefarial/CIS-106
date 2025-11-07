tickets = int(input("Enter number of tickets: "))

if tickets >= 25:
    price = 50.00
elif 10 <= tickets <= 24:
    price = 60.00
elif 5 <= tickets <= 9:
    price = 70.00
else:
    price = 75.00

total = tickets * price

print(f"Tickets: {tickets}")
print(f"Price per ticket: ${price:.2f}")
print(f"Total cost: ${total:.2f}")
