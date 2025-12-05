filename = "employees.txt"

sum_bonus = 0.0
print(f"{'Last Name':<15}{'Salary':>12}{'Bonus':>12}")

with open(filename, "r") as f:
    while True:
        name = f.readline()
        if not name:
            break  
        name = name.strip()

        salary_line = f.readline()
        if not salary_line:
            break  
        salary = float(salary_line.strip())

        if salary >= 100000:
            rate = 0.20
        elif salary >= 50000:
            rate = 0.15
        else:
            rate = 0.10

        bonus = salary * rate
        sum_bonus += bonus
        print(f"{name:<15}${salary:>11,.2f}${bonus:>11,.2f}")

print(f"\nSum of bonuses paid: ${sum_bonus:,.2f}")
