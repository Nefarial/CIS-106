def load_players(filename):
    names = []
    avgs = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) == 2:
                name = parts[0]
                avg = float(parts[1])
                names.append(name)
                avgs.append(avg)
    return names, avgs


def show_players(names, avgs):
    print(f"{'Player':15}{'Average':>10}")
    print("-" * 25)
    for i in range(len(names)):
        print(f"{names[i]:15}{avgs[i]:10.3f}")


def find_player_index(names, target):
    i = 0
    while i < len(names):
        if names[i].lower() == target.lower():
            return i
        i += 1
    return -1


filename = "players.txt"  
player_names, batting_avgs = load_players(filename)

show_players(player_names, batting_avgs)
print()

again = "yes"
while again.strip().lower() == "yes":
    search_name = input("Enter a last name to look up (or press Enter to quit): ")
    if search_name == "":
        break

    index = find_player_index(player_names, search_name)

    if index == -1:
        print("Name not found.")
    else:
        print(f"{player_names[index]} has a batting average of {batting_avgs[index]:.3f}")

    again = input("Do you want to search for another player (Yes or No)? ")

print("Program finished.")
