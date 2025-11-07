principal = float(input("Enter principal amount: "))
years = int(input("Enter years to maturity: "))

if principal > 100000 and years == 5:
    rate = 0.06
elif 50000 <= principal <= 100000 and years == 10:
    rate = 0.05
elif 50000 <= principal <= 100000 and years == 5:
    rate = 0.04
else:
    rate = 0.02

first_year_interest = principal * rate

print(f"Principal: ${principal:.2f}")
print(f"Interest rate: {rate*100:.1f}%")
print(f"First-year interest: ${first_year_interest:.2f}")
