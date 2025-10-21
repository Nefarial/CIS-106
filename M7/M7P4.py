answer = input("Do you want to enter an employee? Yes/No: ")

count = 0
sum = 0.0

while answer == "Yes":
    last_name = input("Enter employee last name: ")
    hours = float(input("Enter hours worked: "))
    rate  = float(input("Enter rate of pay: "))

    if hours > 40:
        gross = 40 * rate + (hours - 40) * rate * 1.5
    else:
        gross = hours * rate

    print(f"{last_name}'s gross pay is: ${gross:.2f}")
    print()

    sum += gross
    count += 1
    answer = input("Enter another employee? Yes/No: ")

avg = (sum / count) if count > 0 else 0.0
print(f"The sum pay of your employees is: ${sum:.2f}")
print(f"The number of employees is: {count}")
print(f"The average pay of your employees is: ${avg:.2f}")
