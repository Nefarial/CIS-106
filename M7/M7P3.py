answer = input("Do you want to enter a student? Yes/No: ")
total = 0

while answer == "Yes":
    last_name = input("Enter last name: ")
    exam1 = float(input("Enter exam 1 score: "))
    exam2 = float(input("Enter exam 2 score: "))
    average = (exam1 + exam2) / 2

    print(f"Student: {last_name}")
    print(f"Average: {average:.2f}")
    print()

    total += 1
    answer = input("Enter another student? Yes/No: ")

print(f"Number of students entered: {total}")
