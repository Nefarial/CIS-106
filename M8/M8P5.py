filename = "students.txt"

sum_tuition = 0.0
count = 0

print(f"{'Last Name':<15}{'Credits':>8}{'Tuition':>12}")

with open(filename, "r") as f:
    while True:
        name = f.readline()
        if not name:
            break
        name = name.strip()

        code = f.readline()
        credits_line = f.readline()
        if not code or not credits_line:
            break

        code = code.strip().upper()
        credits = int(credits_line.strip())

        if code == "I":
            cost = 250.00
        else:  
            cost = 500.00

        tuition = credits * cost
        sum_tuition += tuition
        count += 1

        print(f"{name:<15}{credits:>8}{tuition:>12.2f}")

print(f"\nTotal tuition owed: ${sum_tuition:,.2f}")
print(f"Number of students: {count}")
