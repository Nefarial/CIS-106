def compute_points(scores):
    total = sum(scores)
    average = total / len(scores)
    return total, average

lname = input("Enter student's last name: ")

s1 = float(input("Enter exam 1 score: "))
s2 = float(input("Enter exam 2 score: "))
s3 = float(input("Enter exam 3 score: "))

score_list = [s1, s2, s3]

total, avg = compute_points(score_list)

print("\nLast Name        Total   Average")
print("-" * 32)
print(f"{lname:<15}{total:6.1f}{avg:9.1f}")
