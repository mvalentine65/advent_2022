rock = {
    "X": 4,
    "Y": 8,
    "Z": 3,
}

paper = {"X": 1, "Y": 5, "Z": 9}

scissors = {
    "X": 7,
    "Y": 2,
    "Z": 6,
}

opponent = {"A": rock, "B": paper, "C": scissors}
score = 0
with open("input.txt") as f:
    for line in f:
        fields = line.strip().split()
        score += opponent[fields[0]][fields[1]]
print(f"theoritical score: {score}")

paper2 = {"X": 1, "Y": 5, "Z": 9}

scissors2 = {"X": 2, "Y": 6, "Z": 7}

rock2 = {"X": 3, "Y": 4, "Z": 8}

opponent2 = {"A": rock2, "B": paper2, "C": scissors2}
actual_score = 0
with open("input.txt") as f:
    for line in f:
        fields = line.strip().split()
        actual_score += opponent2[fields[0]][fields[1]]
print(f"suggested score: {actual_score}")
