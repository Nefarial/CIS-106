last_name = input("Enter employee last name: ")
salary = float(input("Enter salary: "))
level = int(input("Enter job level: "))

if level >= 10:
    bonus_rate = 0.25
elif 5 <= level <= 9:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10

bonus = salary * bonus_rate

print(f"Employee: {last_name}")
print(f"Bonus rate: {bonus_rate*100:.0f}%")
print(f"Bonus: ${bonus:.2f}")
