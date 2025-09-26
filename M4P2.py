PPS = float(input("What was the purchase price per share of your stock?: "))

current_price = float(input("What is the current price of your stock?: "))

quantity = int(input("How many shares do you own of this stock?: "))

value = (current_price - PPS) * quantity

print(f"The total value of your stock is ${value:.2f}")

