def show_names(names):
    print("Names (forward):")
    for i in range(len(names)):
        print(names[i])


def show_names_reverse(names):
    print("Names (reverse):")
    i = len(names) - 1
    while i >= 0:
        print(names[i])
        i -= 1


last_names = [
    "Adams", "Baker", "Clark", "Davis", "Evans",
    "Foster", "Green", "Harris", "Irwin", "Jones"
]

show_names(last_names)
print()
show_names_reverse(last_names)
