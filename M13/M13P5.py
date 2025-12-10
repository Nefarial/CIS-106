import math

rooms = {}

again = "yes"

while again.strip().lower() == "yes":
    name = input("Enter room name: ")

    length = float(input("Enter length of the room (feet): "))
    width  = float(input("Enter width of the room (feet): "))
    height = float(input("Enter height of the room (feet): "))

    wall_area = 2 * length * height + 2 * width * height

    gallons = math.ceil(wall_area / 50.0)

    rooms[name] = gallons

    again = input("Do you want to enter another room (Yes or No)? ")

print()
print(f"{'Room':15}{'Gallons':>8}")
print("-" * 23)

for name, gallons in rooms.items():
    print(f"{name:15}{gallons:8d}")
