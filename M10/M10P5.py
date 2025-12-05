def assessed_value(county, market_value):
    """Return assessed value based on county and market value."""
    county = county.strip().lower()

    if county == "cook":
        rate = 0.90
    elif county == "dupage":
        rate = 0.80
    elif county == "mchenry":
        rate = 0.75
    elif county == "kane":
        rate = 0.60
    else:
        rate = 0.70

    assessed = market_value * rate
    return assessed


again = input("Do you want to do the property program (Yes or No)? ")

print("County\tMarket Value\tAssessed Value")
print("---------------------------------------------")

total_market = 0.0
total_assessed = 0.0

while again.strip().lower() == "yes":
    county = input("Enter county name: ")
    market = float(input("Enter market value of the home: "))

    assessed = assessed_value(county, market)

    total_market += market
    total_assessed += assessed

    print(county, end="\t")
    print(f"$ {market:,.2f}", end="\t")
    print(f"$ {assessed:,.2f}")

    again = input("Do you want to enter another property (Yes or No)? ")

print("---------------------------------------------")
print(f"Total market value:\t$ {total_market:,.2f}")
print(f"Total assessed value:\t$ {total_assessed:,.2f}")
