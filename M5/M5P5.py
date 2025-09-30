last_name = input("Enter last name: ")
dependents = int(input("Enter number of dependents: "))
gincome = float(input("Enter gross income: "))

adjgross = gincome - (dependents * 12000)
if adjgross > 50000:
    taxr = .20
else:
    taxr = .10

intax = adjgross * taxr
if intax < 0:
    intax = 100

print("Last Name:", last_name)
print("Gross Income: $", gincome)
print("Dependents:", dependents)
print("Adjusted Gross Income: $", adjgross)
print("Income Tax: $", intax)
