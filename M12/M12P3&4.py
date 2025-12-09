def load_names_scores(filename):
    names = []
    scores = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) == 2:
                name = parts[0]
                score = int(parts[1])
                names.append(name)
                scores.append(score)
    return names, scores


def show_highest(names, scores):
    high_var = 0
    high_index = 0

    i = 0
    while i < len(scores):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
        i += 1

    print("Highest score:")
    print(f"{names[high_index]:15}{high_var:7d}")


def show_lowest(names, scores):
    low_var = 999
    low_index = 0

    i = 0
    while i < len(scores):
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i
        i += 1

    print("Lowest score:")
    print(f"{names[low_index]:15}{low_var:7d}")


filename = "students.txt"  
last_names, exam_scores = load_names_scores(filename)

print(f"{'Name':15}{'Score':>7}")
print("-" * 22)
for i in range(len(last_names)):
    print(f"{last_names[i]:15}{exam_scores[i]:7d}")

print()
show_highest(last_names, exam_scores)
print()
show_lowest(last_names, exam_scores)
