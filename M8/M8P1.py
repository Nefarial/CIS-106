principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (e.g., 0.10 for 10%): "))

beginning = principal
a_interest = 0.0

print("\nFormatted output")
print(f"{'Year':<4} {'Beginning':>12} {'Ending':>12}")
for year in range(1, 6):
    interest = beginning * rate
    end = beginning + interest
    a_interest += interest
    print(f"{year:<4} ${beginning:>11,.2f} ${end:>11,.2f}")
    beginning = end

print(f"\nTotal interest earned (5 yrs): ${a_interest:,.2f}")
