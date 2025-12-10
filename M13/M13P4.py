def load_players_dict(filename):
    players = {}
    with open(filename, "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) == 2:
                name = parts[0]
                avg = float(parts[1])
                players[name] = avg
    return players


filename = "players.txt"
batting_dict = load_players_dict(filename)

again = "yes"

while again.strip().lower() == "yes":
    search_name = input("Enter a last name to look up batting average: ")

    if search_name in batting_dict:
        avg = batting_dict[search_name]
        print(f"{search_name} has a batting average of {avg:.3f}")
    else:
        print("Name not found.")

    again = input("Do you want to look up another player (Yes or No)? ")
