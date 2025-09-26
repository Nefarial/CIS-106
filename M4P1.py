exam1 = float(input("What was your score for the first exam?: "))
while exam1 < 0 or exam1 > 100:
    print("Score must be between 0 and 100.")
    exam1 = float(input("What was your score for the first exam?"))

exam2 = float(input("What was your score for the second exam?: "))
while exam2 < 0 or exam2 > 100:
    print("Score must be between 0 and 100.")
    exam2 = float(input("What was your score for the first exam?"))
    
total = (exam1 * .60) + (exam2 * .40)

print(f"Your total score is {total:.2f}")

