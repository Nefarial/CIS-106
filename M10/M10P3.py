def car_total_price(msrp, make, model, electric):
    if make.lower() == "honda":
        base_rate = 0.10
    elif make.lower() == "toyota":
        base_rate = 0.15
    else:
        base_rate = 0.00

    if electric.lower() == "y":
        electric_rate = 0.30
    else:
        electric_rate = 0.05

    disc_rate = base_rate + electric_rate
    discount = msrp * disc_rate
    new_msrp = msrp - discount
    total = new_msrp * 1.07
    return disc_rate, discount, new_msrp, total

again = input("Do you want to do the car program (Yes or No)? ")
print(f"{'Make':<12}{'Model':<12}{'MSRP':>10}{'Disc%':>10}{'Total':>12}")
print("-" * 56)
sum_msrp = 0.0
sum_total = 0.0

while again.strip().lower() == "yes":
    make = input("Enter make (e.g. Honda): ")
    model = input("Enter model (e.g. Accord): ")
    electric = input("Is the vehicle electric? (Y or N): ")
    msrp = float(input("Enter MSRP (sticker price): "))
    rate, discount, new_msrp, total_price = car_total_price(msrp, make, model, electric)

    sum_msrp += msrp
    sum_total += total_price
    print(f"{make:<12}{model:<12}$ {msrp:>8,.2f}{rate:>9.2%}  $ {total_price:>10,.2f}")
    again = input("Do you want to enter another car (Yes or No)? ")

print("-" * 56)
print(f"Total MSRP of all cars:     $ {sum_msrp:,.2f}")
print(f"Total sales price of cars:  $ {sum_total:,.2f}")
