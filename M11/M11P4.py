def compute_bowling_averages(scores, handicap):
    total = sum(scores)
    avg = total / len(scores)

    adjusted_scores = []
    for score in scores:
        adjusted_scores.append(score + handicap)

    adj_total = sum(adjusted_scores)
    adj_avg = adj_total / len(adjusted_scores)

    return avg, adj_avg

lname = input("Enter bowler's last name: ")

g1 = int(input("Enter game 1 score: "))
g2 = int(input("Enter game 2 score: "))
g3 = int(input("Enter game 3 score: "))

handicap = int(input("Enter handicap per game: "))

games = [g1, g2, g3]

avg, adj_avg = compute_bowling_averages(games, handicap)

print("\nLast Name        Avg   Avg+Handicap")
print("-" * 36)
print(f"{lname:<15}{avg:6.1f}{adj_avg:14.1f}")
