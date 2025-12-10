grades = {
    "Adams": [88, 90, 84],
    "Baker": [92, 95, 91],
    "Clark": [75, 78, 80],
    "Davis": [96, 94, 97],
    "Evans": [84, 82, 86],
    "Foster": [79, 81, 77],
    "Green": [90, 89, 92],
    "Harris": [68, 70, 72],
    "Irwin": [95, 93, 96],
    "Jones": [87, 88, 90]
}

def class_grade_averages(grade_dict):
    """Return a list [avg1, avg2, avg3] for the three grades."""
    total1 = total2 = total3 = 0
    count = 0

    for scores in grade_dict.values():
        total1 += scores[0]
        total2 += scores[1]
        total3 += scores[2]
        count += 1

    avg1 = total1 / count
    avg2 = total2 / count
    avg3 = total3 / count
    return [avg1, avg2, avg3]


print(f"{'Name':15}{'G1':>6}{'G2':>6}{'G3':>6}{'Avg':>8}")
print("-" * 41)

for name, scores in grades.items():
    g1, g2, g3 = scores[0], scores[1], scores[2]
    avg = (g1 + g2 + g3) / 3.0
    print(f"{name:15}{g1:6d}{g2:6d}{g3:6d}{avg:8.2f}")

class_avgs = class_grade_averages(grades)

print("-" * 41)
print(f"{'Class Avg':15}{class_avgs[0]:6.2f}{class_avgs[1]:6.2f}{class_avgs[2]:6.2f}")
