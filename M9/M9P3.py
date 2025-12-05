def miles_per_gallon(miles, gallons):
    """Return miles per gallon."""
    if gallons == 0:
        return 0.0
    return miles / gallons
print(f"{'City':<15}{'Miles':>8}{'Gallons':>10}{'MPG':>8}")
print("-" * 45)

trip_count = 0
total_miles = 0.0
total_gallons = 0.0
again = "Y"

while again.upper() == "Y":
    city = input("Enter destination city: ")
    miles = float(input("Enter miles travelled: "))
    gallons = float(input("Enter gallons used: "))
    mpg = miles_per_gallon(miles, gallons)
    trip_count += 1
    total_miles += miles
    total_gallons += gallons
    print(f"{city:<15}{miles:>8.1f}{gallons:>10.1f}{mpg:>8.1f}")
    again = input("Do you want to enter another trip? (Y/N): ")
    
print("-" * 45)
print(f"Number of trips: {trip_count}")
print(f"Total miles: {total_miles:.1f}")
print(f"Total gallons: {total_gallons:.1f}")
overall_mpg = miles_per_gallon(total_miles, total_gallons)
print(f"Overall MPG: {overall_mpg:.1f}")
