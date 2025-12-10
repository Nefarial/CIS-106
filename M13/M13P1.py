grades = {
    "Adams": 88,
    "Baker": 92,
    "Clark": 75,
    "Davis": 96,
    "Evans": 84,
    "Foster": 79,
    "Green": 90,
    "Harris": 68,
    "Irwin": 95,
    "Jones": 87
}

print(f"{'Name':15}{'Grade':>7}")
print("-" * 22)

total = 0
count = 0

for name, grade in grades.items():
    print(f"{name:15}{grade:7d}")
    total += grade
    count += 1

class_avg = total / count
print("-" * 22)
print(f"{'Class Avg:':15}{class_avg:7.2f}")
