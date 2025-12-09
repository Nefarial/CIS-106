def show_students(names, scores):
    print(f"{'Name':15}{'Score':>7}")
    print("-" * 22)
    for i in range(len(names)):
        print(f"{names[i]:15}{scores[i]:7d}")


def show_students_reverse(names, scores):
    print("Reverse order:")
    print(f"{'Name':15}{'Score':>7}")
    print("-" * 22)
    i = len(names) - 1
    while i >= 0:
        print(f"{names[i]:15}{scores[i]:7d}")
        i -= 1


last_names = [
    "Adams", "Baker", "Clark", "Davis", "Evans",
    "Foster", "Green", "Harris", "Irwin", "Jones"
]

exam_scores = [88, 92, 75, 96, 84, 79, 90, 68, 95, 87]

show_students(last_names, exam_scores)
print()
show_students_reverse(last_names, exam_scores)
