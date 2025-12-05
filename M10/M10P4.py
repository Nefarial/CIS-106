def ticket_price(miles):
    """Return ticket price based on miles from Chicago."""
    if miles >= 30:
        return 12.00
    elif 20 <= miles <= 29:
        return 10.00
    elif 10 <= miles <= 19:
        return 8.00
    else:
        return 5.00

again = input("Do you want to do the train program (Yes or No)? ")

print("Name\tMiles\tTicket")
print("-----------------------------")

total_tickets = 0.0

while again.strip().lower() == "yes":
    lname = input("Enter passenger last name: ")
    miles = int(input("Enter miles from downtown Chicago: "))
    price = ticket_price(miles)

    total_tickets += price

    print(lname, end="\t")
    print(f"{miles} miles", end="\t")
    print(f"$ {price:.2f}")

    again = input("Do you want to enter another passenger (Yes or No)? ")

print("-----------------------------")
print(f"Total price of all tickets: $ {total_tickets:.2f}")
