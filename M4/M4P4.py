first_name = input("Enter your first name: ")
steps = int(input("How many steps did you walk today?: "))

calories = steps * 0.25

print(f"{first_name} has burned {calories:.2f} calories.")
