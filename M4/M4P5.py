cost = float(input("Enter the fixed cost: "))
ppu = float(input("Enter the price per unit: "))
cpu = float(input("Enter the cost per unit: "))

breakeven = cost / (ppu - cpu)

print(f"The break-even point is {breakeven:.2f}")
