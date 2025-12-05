def pay_rate(job_code):
    """Return hourly pay rate based on job code."""
    job_code = job_code.upper()
    if job_code == "L":
        return 25.0
    elif job_code == "A":
        return 30.0
    elif job_code == "J":
        return 50.0
    else:
        return 0.0   
print(f"{'Last Name':<15}{'Gross Pay':>12}")
print("-" * 27)

total_gross = 0.0
again = "Y"
while again.upper() == "Y":
    lname = input("Enter employee last name: ")
    code = input("Enter job code (L, A, J): ")
    hours = float(input("Enter hours worked: "))
    rate = pay_rate(code)
    if hours <= 40:
        pay = hours * rate
    else:
        pay = 40 * rate + (hours - 40) * rate * 1.5
    total_gross += pay
    print(f"{lname:<15}${pay:>11.2f}")
    again = input("Do you want to enter another employee? (Y/N): ")
    
print("-" * 27)
print(f"Total gross pay for all employees: ${total_gross:,.2f}")
