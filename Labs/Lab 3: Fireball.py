num_dice = 5
sides_per_die = 6
rollcount = 0

for die1 in range(1, sides_per_die + 1):
    for die2 in range(1, sides_per_die + 1):
        for die3 in range(1, sides_per_die + 1):
            for die4 in range(1, sides_per_die + 1):
                for die5 in range(1, sides_per_die + 1):
                    print(die1, die2, die3, die4, die5)
                    rollcount += 1

print("Total number of possible rolls:", rollcount)