def batting_average(hits, at_bats):
    """Return batting average = hits / at-bats."""
    if at_bats == 0:
        return 0.0
    return hits / at_bats

print(f"{'Player':<15}{'Average':>10}")
print("-" * 25)
player_count = 0
again = "Y"

while again.upper() == "Y":
    lname = input("Enter player last name: ")
    hits = int(input("Enter number of hits: "))
    at_bats = int(input("Enter number of at-bats: "))
    avg = batting_average(hits, at_bats)
    player_count += 1
    print(f"{lname:<15}{avg:>10.3f}")
    again = input("Do you want to enter another player? (Y/N): ")
    
print("-" * 25)
print(f"Number of players entered: {player_count}")
