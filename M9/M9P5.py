def tuition_owed(credits, dist_code):
    """Return tuition owed based on credits and district code."""
    dist_code = dist_code.upper()
    if dist_code == "I":
        rate = 250.0
    else:             
        rate = 550.0
    return credits * rate

print(f"{'Last Name':<15}{'Credits':>8}{'Tuition':>12}")
print("-" * 35)

total_tuition = 0.0
student_count = 0
again = "Y"
while again.upper() == "Y":
    lname = input("Enter student last name: ")
    credits = int(input("Enter number of credit hours: "))
    code = input("Enter district code (I or O): ")
    tuition = tuition_owed(credits, code)
    total_tuition += tuition
    student_count += 1
    print(f"{lname:<15}{credits:>8d}${tuition:>11.2f}")
    again = input("Do you want to enter another student? (Y/N): ")

print("-" * 35)
print(f"Number of students: {student_count}")
print(f"Total tuition owed: ${total_tuition:,.2f}")
