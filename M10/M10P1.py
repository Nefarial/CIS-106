def forecast_next_month(month, sales):
    """Return rate and forecast based on month."""
    month = month.strip().lower()
    
    if month in ("jan", "feb", "mar", "january", "february", "march"):
        rate = 0.10
    elif month in ("apr", "may", "jun", "april", "june"):
        rate = 0.15
    elif month in ("jul", "aug", "sep", "july", "august", "september"):
        rate = 0.20
    else:
        rate = 0.25
    forecast = sales * (1 + rate)
    return rate, forecast

again = input("Do you want to do the forecast program (Yes or No)? ")
print(f"{'Month':<10}{'Sales':>12}{'Rate':>8}{'Next Month':>14}")
print("-" * 44)
sum_sales = 0.0
sum_forecast = 0.0

while again.strip().lower() == "yes":
    month = input("Enter month: ")
    sales = float(input("Enter this month's sales: "))
    rate, next_sales = forecast_next_month(month, sales)
    sum_sales += sales
    sum_forecast += next_sales
    print(f"{month:<10}${sales:>11.2f}{rate:>7.2f}${next_sales:>13.2f}")
    again = input("Do you want to enter another month (Yes or No)? ")

print("-" * 44)
print(f"{'TOTAL SALES:':<22}${sum_sales:>10.2f}")
print(f"{'TOTAL FORECAST:':<22}${sum_forecast:>10.2f}")
print("\nForecast program complete.")
