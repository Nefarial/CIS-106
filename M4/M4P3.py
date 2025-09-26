food = float(input("What was the cost of your food?: "))

tip15 = food * .15

tip18 = food * .18

tip20 = food * .20

totaltip15 = tip15 + food

totaltip18 = tip18 + food

totaltip20 = tip20 + food

print("With 15% tip: ")
print(f"Total: {food:.2f}")
print(f"Tip: {tip15:.2f}")
print(f"Total with tip: {totaltip15:.2f}")
print()

print("With 18% tip: ")
print(f"Total: {food:.2f}")
print(f"Tip: {tip18:.2f}")
print(f"Total with tip: {totaltip18:.2f}")
print()

print("With 20% tip: ")
print(f"Total: {food:.2f}")
print(f"Tip: {tip20:.2f}")
print(f"Total with tip: {totaltip20:.2f}")
