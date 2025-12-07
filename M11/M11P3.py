def commission_and_target(sales):
    if sales >= 100000:
        comm_rate = 0.10
    else:
        comm_rate = 0.05

    commission = sales * comm_rate
    next_year_target = sales * 1.05
    return commission, next_year_target


again = input("Do you want to enter salesperson data (Yes or No)? ")

print(f"{'Last Name':15}{'Sales':>12}{'Commission':>15}{'Next Year Target':>20}")
print("-" * 62)

total_sales = 0.0
total_commission = 0.0
total_target = 0.0

while again.strip().lower() == "yes":
    lname = input("Enter last name: ")
    sales = float(input("Enter sales amount: "))

    commission, next_target = commission_and_target(sales)

    total_sales += sales
    total_commission += commission
    total_target += next_target

    print(f"{lname:15}${sales:>10,.2f}${commission:>13,.2f}${next_target:>18,.2f}")

    again = input("Do you want to enter another salesperson (Yes or No)? ")

print("-" * 62)
print(f"{'TOTALS':15}${total_sales:>10,.2f}${total_commission:>13,.2f}${total_target:>18,.2f}")
