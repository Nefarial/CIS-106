COVERAGE_PER_GALLON = 50.0  

def wall_area(length, width, height):
    """Return total wall square footage of the room."""
    
    return 2 * length * height + 2 * width * height
def rect_area(length, width):
    """Return area of ceiling or floor (length x width)."""
    return length * width

def gallons_needed(area):
    """Return gallons needed for a given area."""
    return area / COVERAGE_PER_GALLON

again = input("Do you want to do the paint program (Yes or No)? ")
while again.strip().lower() == "yes":
    length = float(input("Enter room length (feet): "))
    width = float(input("Enter room width (feet): "))
    height = float(input("Enter room height (feet): "))
    w_area = wall_area(length, width, height)
    wall_gallons = gallons_needed(w_area)
    
    print(f"\nWall area: {w_area:.2f} square feet")
    print(f"Gallons needed for walls: {wall_gallons:.2f}")
          
    cf_area = rect_area(length, width)
    cf_gallons = gallons_needed(cf_area)
          
    print(f"Ceiling/floor area: {cf_area:.2f} square feet")
    print(f"Gallons needed for ceiling or floor: {cf_gallons:.2f}\n")
    again = input("Do you want to do another room (Yes or No)? ")

print("Paint program finished.\n")
