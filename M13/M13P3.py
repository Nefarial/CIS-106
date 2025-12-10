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

print(f"{'Player':15}{'Average':>10}")
print("-" * 25)

for name, avg in batting_dict.items():
    print(f"{name:15}{avg:10.3f}")
